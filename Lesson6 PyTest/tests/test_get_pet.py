import random
from pprint import pprint

import requests

dct = {
    "base_url": "https://petstore.swagger.io/v2",
    "get_pet_by_url": "/pet/",
    "create_pet_url": "/pet"
}

base_url = "https://petstore.swagger.io/v2"
get_pet_by_url = "/pet/"
create_pet_url ="/pet"


# response = requests.get(full_url)
# print(response)


def test_create_pet():
    full_url = base_url + create_pet_url
    pet_id = random.randint(10000, 100000)
    with open("pet_created_id.txt", "w", encoding="utf-8") as file:
        file.write(f"{pet_id}")

    data = {
        "category": {
            "id": 3,
            "name": "string"
        },
        "id": pet_id,
        "name": "Chara",
        "photoUrls": [
            "string"
        ],
        "status": "string",
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ]
    }

    response = requests.post(full_url, json=data)
    print()
    # status_code = response.status_code
    # print(status_code)
    body = response.json()
    # print(body)
    print("==========================")
    pprint(body)
    print("==========================")

    full_url1 = f"{base_url}{get_pet_by_url}{pet_id}"
    response1 = requests.get(full_url1)
    pprint(response1.json())


#
# def test_update_pet():
#     # pass
#     full_url = base_url + create_pet_url
#     with open("pet_created_id.txt", "r", encoding="utf-8") as file:
#         pet_id = file.readline().strip()
#             data = {
#                 "category": {
#                     "id": 2,
#                     "name": "Dude"
#                 },
#                 "id": pet_id,
#                 "name": "taksa",
#                 "photoUrls": [
#                     "string"
#                 ],
#                 "status": "string",
#                 "tags": [
#                     {
#                         "id": 0,
#                         "name": "string"
#                     }
#                 ]
#             }
#         response = requests.put(full_url, json=data)
#         data = response.json()
#         print("====================================")
#         pprint(data)
#         print("====================================")
#         full_url1 = f"{base_url}{get_pet_by_url}{pet_id}"
#         response1 = requests.get(full_url1)
#         pprint(response1.json())


def test_delete_pet():
    with open("pet_created_id.txt", "r", encoding="utf-8") as file:
        pet_id = file.readline().strip()
    full_url = f"{base_url}{get_pet_by_url}{pet_id}"
    response = requests.delete(full_url)
    # pprint(response.json())

    print("=============================")
    print(response.status_code)
    assert response.status_code == 200

    full_url1 = f"{base_url}{get_pet_by_url}{pet_id}"
    response1 = requests.get(full_url1)
    # pprint(response1.json())

    assert response.status_code == 200