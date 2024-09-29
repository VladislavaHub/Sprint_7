import allure

from data import CreateCourier
from new_user import NewUser
from interface_api import InterfaceApi


class TestCreatingACourier:

    @allure.description('Проверка успешного создания курьера с уникальными рандомными данными ')
    def test_create_new_courier_success(self):
        body = NewUser.register_new_courier_and_return_login_password()
        create_response = InterfaceApi.create_courier_endpoint(body)
        courier_id = InterfaceApi.login_endpoint(NewUser.create_body_for_create_order(body)).json()['id']
        assert (courier_id.status_code == 201 and create_response.json() == CreateCourier.CREATE_SUCCESS_RESPONSE)

    @allure.title('Проверка создания курьера с повторяющимся логином')
    def test_create_two_same_courier(self):
        body = NewUser.register_new_courier_and_return_login_password()
        InterfaceApi.create_courier_endpoint(body)
        create_response = InterfaceApi.create_courier_endpoint(body)
        assert (create_response.status_code == 409 and create_response.json()['message'] == CreateCourier.TEXT_ERROR_CREATE_409)

    @allure.title('Проверка создания курьера без пароля')
    def test_create_new_courier_without_pass(self):
        create_response = InterfaceApi.create_courier_endpoint(NewUser.create_body_for_create_order())
        assert (create_response.status_code == 400 and create_response.json()['message'] == CreateCourier.TEXT_ERROR_CREATE_400)

    @allure.title('Проверка создания курьера без логина')
    def test_create_new_courier_without_login(self):
        create_response = InterfaceApi.create_courier_endpoint(NewUser.create_body_for_create_order())
        assert (create_response.status_code == 400 and create_response.json()['message'] == CreateCourier.TEXT_ERROR_CREATE_400)