import json
import pytest
import requests
import allure
from data import Orders
from urls import Urls
from endpoints import Endpoints

class TestCreateOrder:
    @pytest.mark.parametrize("colors", [["BLACK"], ["GREY"], [], ["BLACK", "GREY"]])
    @allure.title("Создание заказа с параметром цвета")
    def test_create_order_colors(self, colors):
        order_data = Orders.base.copy()
        order_data["color"] = colors
        response = requests.post(
            f"{Urls.BASE_URL}{Endpoints.CREATE_ORDER}",
            data=json.dumps(order_data),
            headers={"Content-Type": "application/json"}
        )
        assert response.status_code == 201 and "track" in response.text
