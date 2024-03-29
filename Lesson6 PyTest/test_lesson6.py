import pytest
import requests
# requests # needed to work with API


base_url = 'https://restful-booker.herokuapp.com/booking'
auth_url = 'https://restful-booker.herokuapp.com/auth'
@pytest.fixture(scope='module') # встроенная в PyChar текстура (text  в имени не нужен)
def auth_token(): # previous name (when we didn't use fixture) was get_auth_token
    authdata = {
        'username': 'admin',
        'password': 'password123'
    }
    response = requests.post(auth_url, json=authdata)
    token = response.json()["token"]
    yield token # if we decided to use fixture -> then instead of print we should use yield, cause fixture
                # will be provided in parameters of each test methods
    # print(token)
    assert response.status_code == 200

@pytest.fixture(scope='session')
def booking_id():  #this method with fixture we created instead of text_create_booking() method withod fixture (see below)
    payload = {
            "firstname": "Johny",
            "lastname": "Smith",
            "totalprice": 1200,
            "depositpaid": False,
            "bookingdates": {
                "checkin": "2024-01-01",
                "checkout": "2025-01-20"
            },
            "additionalneeds": "Breakfast"
        }

    response = requests.post(base_url, json=payload)
    yield response.json()['bookingid']


# def sum_it(x,y):
#     return x + y
#
# def test_not_equal():
#     assert sum_it(543, 324) == 877
#
#
# def test_equal():
#     assert sum_it(32, 43) == 75

@pytest.mark.slow
@pytest.mark.smoke # we created this custom marker smoke in the pytest.ini file
def test_get_code():
    result = requests.get(base_url)
    assert result.status_code == 200
    print(result)


@pytest.mark.regression
@pytest.mark.xfail(reason='invalid configuration or selector') # mark with this fixture tests that may fall with certain
def test_get_booking_by_id(booking_id):
    response = requests.get(f'{base_url}/{booking_id}')
    response_data = response.json()
    expected_keys = [
        'firstname', 'lastname','totalprice','depositpaid','bookingdates','additionalneeds'
    ]

    assert response.status_code == 200
    print(response_data)
    assert len(response_data.keys()) == len(expected_keys)
    for key in expected_keys:
        assert key in response_data.keys()


# def test_create_booking():
#     payload = {
#     "firstname" : "Johny",
#     "lastname" : "Smith",
#     "totalprice" : 1200,
#     "depositpaid" : False,
#     "bookingdates" : {
#         "checkin" : "2024-01-01",
#         "checkout" : "2025-01-20"
#     },
#     "additionalneeds" : "Breakfast"
#  }
#
#     response1 = requests.post(base_url, json=payload)
#     print(response1.json()['bookingid'])
#     assert response1.status_code == 200



def test_check_booking(booking_id):
    response2 = requests.get(f'{base_url}/{booking_id}')
    print(response2.json())
    assert response2.status_code == 200
    assert response2.json()['firstname'] == 'Johny'


def test_update_booking(auth_token, booking_id): # auth_token is in parameters cause we have corresponding fixture (see above)
                                                # boooking_id is a method above with fixture (to create booking id)
    payload1 = {
    "firstname" : "Johny",
    "lastname" : "Smith",
    "totalprice" : 1200,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2024-01-01",
        "checkout" : "2024-01-20"
    },
    "additionalneeds" : "Breakfast"
 }

    token = {"cookie": f"token={auth_token}"} # format before swithch to fixture("cookie": "token=16b81c00c48b253")
                                               # was taken from api spec:  -H 'Cookie: token=abc123'

    response3 = requests.put(f'{base_url}/{booking_id}]',json=payload1, headers=token)  # in f-string initially
                                                 # was: {base_url}/1269 but we replaced with the method
                                                # booking_id that creates new booking id
    assert response3.status_code == 200
    response4 = requests.get(f'{base_url}/{booking_id}')
    assert response4.json()['depositpaid'] == True
    print(response4.json())

@pytest.mark.skip
def test_options():
    response = requests.options(f'{base_url}/1')
    assert response.status_code == 200
    print(response.json())


def test_headers():
    response = requests.head(f'{base_url}/1')
    assert response.status_code == 200
    print(response.headers)


def test_booking_delete(booking_id, auth_token):
    token = {"Cookie": f'token ={auth_token}'}
    response = requests.delete(f'{base_url}/{booking_id}', headers=token)
    assert response.status_code == 201
    response_get = requests.get(f'{base_url}/{booking_id}')
    assert response_get.status_code == 403



# Fixtures
# ФИКСТУРЫ В КОНТЕКСТЕ PYTEST — ЭТО ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ДЛЯ ТЕСТОВ. ОНИ НЕ ЯВЛЯЮТСЯ ЧАСТЬЮ ТЕСТОВОГО СЦЕНАРИЯ.
# В PYTEST ФИКСТУРЫ МОЖНО ЗАДАВАТЬ ГЛОБАЛЬНО, ПЕРЕДАВАТЬ ИХ В ТЕСТОВЫЕ МЕТОДЫ КАК ПАРАМЕТРЫ, PYTEST ТАКЖЕ
# ИМЕЕТ НАБОР ВСТРОЕННЫХ ФИКСТУР.
# ФИКСТУРЫ ОБЕСПЕЧИВАЮТ НАДЕЖНОСТЬ ТЕСТОВ, СОГЛАСОВАННОСТЬ И ПОВТОРЯЕМОСТЬ ИХ РЕЗУЛЬТАТОВ. ПРИ ИНИЦИАЛИЗАЦИИ
# МОЖНО НАСТРАИВАТЬ СЕРВИСЫ, СОСТОЯНИЯ, ПЕРЕМЕННЫЕ ОКРУЖЕНИЯ.
# ДЛЯ ФИКСТУР МОЖНО ЗАДАВАТЬ ОБЛАСТЬ ПОКРЫТИЯ (SCOPE). НАПРИМЕР, “FUNCTION”, “CLASS”, “MODULE”, “SESSION”.
# СООТВЕТСТВЕННО, ФИКСТУРА БУДЕТ ВЫЗЫВАТЬ 1 РАЗ ЛИБО ДЛЯ ТЕСТОВОГО МЕТОДА, ЛИБО ДЛЯ КЛАССА, МОДУЛЯ ИЛИ СЕССИИ

# to rusn all tests via terminal: pytest -s -v
# to run tests based on specific marker: pytest -m "smoke" - where smoke is  a custom marker created in pytest.ini file
# to run test with 2 markers (pytest.mark.regression and pytest.mark.xfail) only with one: pytest -v -m 'regression'

import re

# Option 1
def validate_usr(username):
    pattern = r'[a-z0-9_]{4,16}'
    print(username)
    x = re.fullmatch(pattern, username)
    print(x)
    #     return bool(x)
    if x is not None:
        return True
    else:
        return False

# Option 2
def validate_usr(username):
    pattern = r'[a-z0-9_]{4,16}'
    print(username)
    x = re.fullmatch(pattern, username)
    return bool(x)
