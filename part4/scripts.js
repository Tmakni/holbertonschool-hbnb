console.log('Enhanced scripts.js loaded');

document.addEventListener('DOMContentLoaded', () => {
  refreshLoginVisibility();

  if (document.body.id === 'index-page') {
    initIndexPage();
  } else if (document.body.id === 'place-page') {
    initPlacePage();
  } else if (document.body.id === 'login-page') {
    initLoginPage();
  }
});

function getCookie(name) {
  const match = document.cookie.match(new RegExp('(?:^|; )' + name + '=([^;]*)'));
  return match ? decodeURIComponent(match[1]) : null;
}

function setCookie(name, value, days = 7) {
  const expires = new Date(Date.now() + days * 864e5).toUTCString();
  document.cookie = `${name}=${encodeURIComponent(value)}; expires=${expires}; path=/`;
}

function deleteCookie(name) {
  document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/`;
}

function isLoggedIn() {
  return !!getCookie('session_id');
}

function refreshLoginVisibility() {
  const loginLink = document.getElementById('login-link');
  if (loginLink) {
    loginLink.style.display = isLoggedIn() ? 'none' : 'block';
  }
}

/*** INDEX PAGE ***/
function initIndexPage() {
  setupPriceFilter();
  fetchPlaces();
}

async function fetchPlaces() {
  const container = document.getElementById('places-list');
  container.innerHTML = '<p>Loading places…</p>';

  const headers = {};
  const token = getCookie('session_id');
  if (token) headers['Authorization'] = `Bearer ${token}`;

  try {
    const response = await fetch('http://localhost:5001/api/v1/places/', { headers });
    if (response.status === 401) throw new Error('Unauthorized');
    if (!response.ok) throw new Error(`Error ${response.status}`);
    const places = await response.json();
    renderPlaces(places);
  } catch (err) {
    console.error('fetchPlaces error:', err);
    container.innerHTML = `<p class="error">Failed to load places: ${err.message}</p>`;
  }
}

function renderPlaces(places) {
  const container = document.getElementById('places-list');
  container.innerHTML = '';
  places.forEach(p => {
    const card = document.createElement('div');
    card.className = 'place-card';
    card.dataset.price = p.price_by_night || p.price;
    card.innerHTML = `
      <h3>${p.name || p.title}</h3>
      <p>Price: ${p.price_by_night || p.price}€/night</p>
      <button class="details-btn">View Details</button>
    `;
    card.querySelector('.details-btn').addEventListener('click', () => {
      window.location.href = `place.html?id=${p.id}`;
    });
    container.appendChild(card);
  });
}

function setupPriceFilter() {
  const filter = document.getElementById('price-filter');
  const options = ['All', '100', '150', '200'];
  options.forEach(val => {
    const opt = document.createElement('option');
    opt.value = val === 'All' ? '' : val;
    opt.textContent = val;
    filter.appendChild(opt);
  });
  filter.addEventListener('input', debounce(e => {
    const max = e.target.value;
    document.querySelectorAll('.place-card').forEach(card => {
      const price = parseFloat(card.dataset.price);
      card.style.display = (!max || price <= +max) ? '' : 'none';
    });
  }, 300));
}

/*** PLACE DETAIL PAGE ***/
async function initPlacePage() {
  const placeId = new URLSearchParams(window.location.search).get('id');
  if (!placeId) return console.error('No id param');

  refreshLoginVisibility();
  toggleReviewForm(placeId);
  await loadPlaceDetails(placeId);
}

async function loadPlaceDetails(id) {
  const info = document.getElementById('place-details');
  info.innerHTML = '<p>Loading details…</p>';

  const headers = {};
  const token = getCookie('session_id');
  if (token) headers['Authorization'] = `Bearer ${token}`;

  try {
    const res = await fetch(`http://127.0.0.1:5001/api/v1/places/${id}/`, { headers });
    if (res.status === 401) throw new Error('Unauthorized');
    if (!res.ok) throw new Error(`Error ${res.status}`);
    const place = await res.json();
    displayPlaceDetails(place);
  } catch (err) {
    console.error('loadPlaceDetails error:', err);
    info.innerHTML = `<p class="error">Cannot load details: ${err.message}</p>`;
  }
}

function displayPlaceDetails(p) {
  document.getElementById('place-details').innerHTML = `
    <h2>${p.name || p.title}</h2>
    <p><strong>Host:</strong> ${p.user.first_name} ${p.user.last_name}</p>
    <p><strong>Price per night:</strong> ${p.price_by_night || p.price}/</p>
    <p>${p.description}</p>
    <ul>${(p.amenities || []).map(a => `<li>${a.name}</li>`).join('')}</ul>
  `;
  const reviews = document.getElementById('reviews');
  reviews.innerHTML = `<h3>Reviews</h3>`;
  (p.reviews || []).forEach(r => {
    reviews.innerHTML += `
      <div class="review-card">
        <p><b>${r.user.first_name} ${r.user.last_name}</b> on ${new Date(r.created_at).toLocaleDateString()}</p>
        <p>${r.text}</p>
        <p>${'★'.repeat(r.rating)}${'☆'.repeat(5 - r.rating)}</p>
      </div>
    `;
  });
}

function toggleReviewForm(placeId) {
  const token = getCookie('session_id');
  const section = document.getElementById('add-review');
  if (!section) return;
  section.style.display = token ? '' : 'none';
  if (token) setupReviewForm(placeId);
}

function setupReviewForm(placeId) {
  document.getElementById('review-form').addEventListener('submit', async e => {
    e.preventDefault();
    const text = e.target['review-text'].value;
    const rating = +e.target.rating.value;
    await postReview(placeId, { text, rating });
    e.target.reset();
    await loadPlaceDetails(placeId);
  });
}

async function postReview(placeId, { text, rating }) {
  const headers = { 'Content-Type': 'application/json' };
  const token = getCookie('session_id');
  if (token) headers['Authorization'] = `Bearer ${token}`;
  try {
    const res = await fetch(`http://localhost:5001/api/v1/places/${placeId}/reviews/`, {
      method: 'POST',
      headers,
      body: JSON.stringify({ text, rating, place_id: placeId })
    });
    if (!res.ok) throw new Error(`Status ${res.status}`);
    alert('Review posted!');
  } catch (err) {
    console.error('postReview error:', err);
    alert('Unable to post review: ' + err.message);
  }
}

/*** LOGIN PAGE ***/
function initLoginPage() {
  document.getElementById('login-form').addEventListener('submit', async e => {
    e.preventDefault();
    const email = e.target.email.value;
    const password = e.target.password.value;
    try {
      const res = await fetch('http://localhost:5001/api/v1/auth_session/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password })
      });
      if (!res.ok) throw new Error(`Status ${res.status}`);
      // Backend sets session_id cookie
      window.location.href = 'index.html';
    } catch (err) {
      console.error('login error:', err);
      alert('Login error: ' + err.message);
    }
  });
}

/*** UTILITY: Debounce ***/
function debounce(fn, wait) {
  let timeout;
  return (...args) => {
    clearTimeout(timeout);
    timeout = setTimeout(() => fn(...args), wait);
  };
}
