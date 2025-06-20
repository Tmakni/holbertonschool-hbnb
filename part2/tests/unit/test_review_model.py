import pytest
from app.models.review import Review
from app.models.user   import User
from app.models.place  import Place

@pytest.fixture
def sample_user_place():
    # 1) Crée un user et un place valides
    u = User(first_name="Alice", last_name="Dupont", email="alice@example.com")
    p = Place(
        title="Studio", description="Test", price=20.0,
        latitude=48.85, longitude=2.35, owner=u
    )
    return u, p

def test_create_valid_review(sample_user_place):
    user, place = sample_user_place
    rev = Review(text="Super séjour", rating=5, place=place, user=user)
    assert rev.text == "Super séjour"
    assert rev.rating == 5
    # Vérifie que les foreign-keys sont bien stockées
    assert rev.place_id == place.id
    assert rev.user_id  == user.id

@pytest.mark.parametrize("bad_text", ["", 123, "x"*1001])
def test_text_validation_raises(bad_text, sample_user_place):
    user, place = sample_user_place
    with pytest.raises((TypeError, ValueError)):
        Review(text=bad_text, rating=4, place=place, user=user)

@pytest.mark.parametrize("bad_rating", [0, 6, "five"])
def test_rating_validation_raises(bad_rating, sample_user_place):
    user, place = sample_user_place
    with pytest.raises((TypeError, ValueError)):
        Review(text="OK", rating=bad_rating, place=place, user=user)

def test_update_changes_and_timestamps(sample_user_place):
    user, place = sample_user_place
    rev = Review(text="Bien", rating=3, place=place, user=user)
    old_ts = rev.updated_at
    # Modifie à la fois le texte et la note
    rev.update({"text": "Excellent", "rating": 4})
    assert rev.text == "Excellent"
    assert rev.rating == 4
    assert rev.updated_at > old_ts

def test_to_dict_contains_all_fields(sample_user_place):
    user, place = sample_user_place
    rev = Review(text="Test", rating=2, place=place, user=user)
    d = rev.to_dict()
    for key in ("id","text","rating","place_id","user_id","created_at","updated_at"):
        assert key in d
