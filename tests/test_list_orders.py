import requests
import allure
from urls import Urls
from endpoints import Endpoints

class TestListOrders:
    @allure.title("Получение списка заказов")
    def test_list_orders(self):
        response = requests.get(f"{Urls.BASE_URL}{Endpoints.GET_ORDERS}")
        assert response.status_code == 200 and "orders" in response.json()
