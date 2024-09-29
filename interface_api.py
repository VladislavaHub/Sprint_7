import requests

from urls import Urls


class InterfaceApi:

    @staticmethod
    def login_endpoint(body):
        return requests.post(f'{Urls.BASE_URL}{Urls.LOGIN_COURIER_ENDPOINT}', json=body)

    @staticmethod
    def create_courier_endpoint(body):
        return requests.post(f'{Urls.BASE_URL}{Urls.CREATE_COURIER_ENDPOINT}', json=body)

    @staticmethod
    def create_order_endpoint(body):
        return requests.post(f'{Urls.BASE_URL}{Urls.CREATE_ORDER_ENDPOINT}', json=body)

    @staticmethod
    def get_list_order_endpoint():
        return requests.get(f'{Urls.BASE_URL}{Urls.ORDER_LIST_ENDPOINT}')

    @staticmethod
    def get_order_to_track(payload):
        return requests.get(f'{Urls.BASE_URL}{Urls.GET_ORDER_TO_TRACK}', params=payload)