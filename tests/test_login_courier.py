import pytest
import requests
import allure
from urls import Urls
from endpoints import Endpoints

class TestLoginCourier:
    @allure.title("Успешная авторизация возвращает id")
    def test_login_success(self, new_courier):
        credentials = {
            "login": new_courier["login"],
            "password": new_courier["password"]
        }
        response = requests.post(f"{Urls.BASE_URL}{Endpoints.LOGIN_COURIER}", data=credentials)
        assert response.status_code == 200 and "id" in response.text

    @allure.title("Ошибка при неверных данных")
    def test_login_invalid(self):
        invalid = {"login": "test181920", "password": "wrongpass"}
        response = requests.post(f"{Urls.BASE_URL}{Endpoints.LOGIN_COURIER}", data=invalid)
        assert response.status_code == 404

    @pytest.mark.parametrize("data", [
        {"password": "123456"},
        {"login": "testuser"}
    ])
    @allure.title("Ошибка при отсутствии обязательных полей")
    def test_login_missing_field(self, data):
        response = requests.post(f"{Urls.BASE_URL}{Endpoints.LOGIN_COURIER}", data=data)
        assert response.status_code == 400
