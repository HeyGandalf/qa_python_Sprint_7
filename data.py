class Users:
    invalid = {"login": "test181920", "password": "wrongpass"}
    missing_login = {"password": "123456"}
    missing_password = {"login": "testuser"}

class Orders:
    base = {
        "firstName": "Test",
        "lastName": "Testov",
        "address": "MSK, street 5555.",
        "metroStation": 5,
        "phone": "+7 111 222 33 33",
        "rentTime": 6,
        "deliveryDate": "2024-04-25",
        "comment": "Test"
    }
