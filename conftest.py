import pytest
import requests
from urls import Urls
from endpoints import Endpoints
from generator import generate_courier

@pytest.fixture(scope="function")
def new_courier():
    data = generate_courier()
    response = requests.post(f"{Urls.BASE_URL}{Endpoints.CREATE_COURIER}", data=data)
    courier_id = response.json().get("id")
    yield data
    if courier_id:
        requests.delete(f"{Urls.BASE_URL}{Endpoints.CREATE_COURIER}/{courier_id}")
