console.log('scripts.js loaded');

document.addEventListener('DOMContentLoaded', () => {
  checkAuthentication();
  setupPriceFilter();
});

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
  return null;
}

function checkAuthentication() {
  const token = getCookie('token');
  const loginLink = document.getElementById('login-link');

  if (!token) {
    loginLink.style.display = 'block';
  } else {
    loginLink.style.display = 'none';
    fetchPlaces(token);
  }
}

async function fetchPlaces(token) {
  try {
    const response = await fetch('http://localhost:5000/api/v1/places', {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    });

    if (!response.ok) throw new Error('Failed to fetch places');

    const places = await response.json();
    displayPlaces(places);
    window.allPlaces = places;
  } catch (error) {
    console.error('Error fetching places:', error.message);
  }
}

function displayPlaces(places) {
  const list = document.getElementById('places-list');
  list.innerHTML = '';

  places.forEach(place => {
    const placeDiv = document.createElement('div');
    placeDiv.className = 'place-card';
    placeDiv.dataset.price = place.price;

    placeDiv.innerHTML = `
      <h2>${place.name}</h2>
      <p>Price: ${place.price}€/night</p>
      <button class="details-button">View Details</button>
    `;

    list.appendChild(placeDiv);
  });
}

function setupPriceFilter() {
  const filter = document.getElementById('price-filter');
  const prices = [10, 50, 100, 'All'];

  prices.forEach(p => {
    const option = document.createElement('option');
    option.value = p;
    option.textContent = p;
    filter.appendChild(option);
  });

  filter.addEventListener('change', (event) => {
    const selected = event.target.value;
    const list = document.getElementById('places-list');
    const cards = list.getElementsByClassName('place-card');

    for (let card of cards) {
      const price = parseFloat(card.dataset.price);
      if (selected === 'All' || price <= parseFloat(selected)) {
        card.style.display = 'block';
      } else {
        card.style.display = 'none';
      }
    }
  });
}
