import allure
import pytest

from data import CreateOrder
from new_user import NewUser
from interface_api import InterfaceApi


class TestCreatingAnOrder:
    @pytest.mark.parametrize(CreateOrder.param, CreateOrder.value)
    @allure.title('Проверка создания заказа')
    def test_create_order_success(self, first_name, last_name, address, metro_station, phone, rent_time,delivery_date, comment, color):
        body_request = NewUser.create_body_for_create_order(first_name, last_name, address, metro_station,phone, rent_time, delivery_date, comment, color)
        create_response = InterfaceApi.create_order_endpoint(body_request)
        order_track = NewUser.generate_payload_to_get_track(create_response.json()['track'])
        assert order_track.status_code == 201 and 'track' in create_response.text