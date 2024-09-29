class Login:
    # Данные для успешной авторизации курьера
    LOGIN_COURIER_BODY_SUCCESS = {
        "login": "Ira",
        "password": "1111"
    }
    # Данные для авторизации с несуществующим логином
    LOGIN_COURIER_NON_EXISTENT_BODY = {
        "login": "Lol",
        "password": "1111"
    }
    # Данные для авторизации без пароля
    LOGIN_COURIER_BODY_WITHOUT_PASS = {
        "login": "Ira",
        "password": ""
    }
    # Данные для авторизации с неверным паролем
    LOGIN_COURIER_BODY_FALSE_PASS = {
        "login": "Ira",
        "password": "123"
    }

    TEXT_ERROR_LOGIN_404 = "Учетная запись не найдена" # Текст ошибки при авторизации с несуществующими паролем и логином

    TEXT_ERROR_LOGIN_400 = "Недостаточно данных для входа" # Текст ошибки при авторизации без логина или пароля

    COURIER_SUCCESS_ID = 495535 # Id существующего курьера


class CreateCourier:

    CREATE_SUCCESS_RESPONSE = {"ok": True} # Тело ответа при успешном создании курьера

    TEXT_ERROR_CREATE_409 = "Этот логин уже используется" # Текст ошибки при создании курьера с повторяющимся логином

    TEXT_ERROR_CREATE_400 = "Недостаточно данных для создания учетной записи" # Текст ошибки при создании курьера без логина или пароля


class CreateOrder:

    param = 'first_name, last_name, address, metro_station, phone, rent_time, delivery_date, comment, color'
    value = [
        ['Ангелина', 'Иванова', 'Пушкина, д.7', '1', '+79111111567', '7', '2024-10-01', '', ["BLACK"]],
        ['Саня', 'Пудров', 'Лермонтова, д.69', '3', '+79163971111', '1', '2024-10-11', '', [""]],
        ['Stas', 'Rock', 'ул.Победы, д.18', '8', '+79131111100', '1', '2024-10-05', '', ["GREY"]],
        ['Ирина', 'Межрева', 'ул.Тараса, д.75', '1', '+79134333316', '4', '2024-10-03', '', ["BLACK", "GREY"]],
    ]
    # Данные для успешного создания заказа
    CREATE_ORDER_BODY = {
        "firstName": "Влада",
        "lastName": "Хрусталева",
        "address": "Konoha, 142 apt.",
        "metroStation": 1,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2024-10-10",
        "comment": "Возможно будет возможно",
        "color": [
            "BLACK"
        ]
    }