import pytest
from faker import Faker
from rest_framework.test import APIClient
from app.models import Movie


faker = Faker()


def fake_movie_data():
    movie_data = {
        "title": f"{faker.job()} {faker.first_name()}",
        "description": faker.sentence(),
        "year": int(faker.year()),
        "director": faker.name(),
    }
    return movie_data
    

def create_fake_movie():
    movie_data = fake_movie_data()
    new_movie = Movie.objects.create(**movie_data)
    

@pytest.fixture
def client():
    client = APIClient()
    return client


@pytest.fixture
def set_up():
    for i in range(3):
        create_fake_movie()


@pytest.mark.django_db
def test_get_movie_list(client, set_up):
    response = client.get("/movies/", {}, format='json')
    print(len(response.data))

    assert Movie.objects.count() == len(response.data)


@pytest.mark.django_db
def test_get_movie_detail(client, set_up):
    movie = Movie.objects.first()
    response = client.get(f"/movies/{movie.slug}/", {}, format='json')

    for field in ("title", "year", "description", "director"):
        assert field in response.data
        
        
@pytest.mark.django_db
def test_delete_movie(client, set_up):
    movie = Movie.objects.first()
    response = client.delete(f"/movies/{movie.slug}/", {}, format='json')
    movie_pks = [movie.pk for movie in Movie.objects.all()]
    assert movie.pk not in movie_pks
    
    
@pytest.mark.django_db
def test_update_movie(client, set_up):
    movie = Movie.objects.first()
    response = client.get(f"/movies/{movie.slug}/", {}, format='json')
    movie_data = response.data
    new_year = int(faker.year())
    movie_data["year"] = new_year
    response = client.patch(f"/movies/{movie.slug}/", movie_data, format='json')
    movie_obj = Movie.objects.get(pk=movie.pk)
    assert movie_obj.year == new_year
    