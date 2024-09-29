import allure

from interface_api import InterfaceApi


class TestListOfOrders:

    @allure.title('Получение списка заказов')
    def test_list_of_orders(self):
        response = InterfaceApi.get_list_order_endpoint()
        assert response.status_code == 200 and len(response.json()) > 0