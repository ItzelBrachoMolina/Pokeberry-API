import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client



def test_index_redirect():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 302

def test_berries(client):
    response = client.get('/berries')
    assert response.status_code == 200


def test_data(client):
    response = client.get('/allBerryStats')
    assert response.status_code == 200
    assert b"Pokeberries Statistics" in response.data
    assert b"Min Growth Time" in response.data


@pytest.mark.parametrize('path', ['/allBerryStats/headers'])
def test_endpoints(client, path):
    response = client.get(path)
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'


