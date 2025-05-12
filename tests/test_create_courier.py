import allure
import requests
from urls import Urls
from endpoints import Endpoints
from generator import generate_courier, generate_courier_missing_field

class TestCreateCourier:
    @allure.title("Создание курьера")
    def test_create_courier(self):
        courier = generate_courier()
        response = requests.post(f"{Urls.BASE_URL}{Endpoints.CREATE_COURIER}", data=courier)
        assert response.status_code == 201 and response.json().get("ok") is True

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier(self):
        courier = generate_courier()
        requests.post(f"{Urls.BASE_URL}{Endpoints.CREATE_COURIER}", data=courier)
        response = requests.post(f"{Urls.BASE_URL}{Endpoints.CREATE_COURIER}", data=courier)
        assert response.status_code == 409 and "Этот логин уже используется" in response.text

    @allure.title("Ошибка при создании курьера без логина")
    def test_create_courier_without_login(self):
        data = generate_courier_missing_field("login")
        response = requests.post(f"{Urls.BASE_URL}{Endpoints.CREATE_COURIER}", data=data)
        assert response.status_code == 400

    @allure.title("Ошибка при создании курьера без пароля")
    def test_create_courier_without_password(self):
        data = generate_courier_missing_field("password")
        response = requests.post(f"{Urls.BASE_URL}{Endpoints.CREATE_COURIER}", data=data)
        assert response.status_code == 400
