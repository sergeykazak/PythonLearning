import requests
import pydantic
# from pydentic import BaseModel, field_validator

dct = {
    "base_url": "https://petstore.swagger.io/v2",
    "get_pet_by_url": "/pet/",
    "create_pet_url": "/pet"
}

base_url = dct["base_url"]
get_pet_by_url = dct["get_pet_by_url"]
create_pet_url = dct["create_pet_url"]


def test_get_pet_by_id():
    with open("pet_created_id.txt", "r", encoding="utf-8") as file:
        pet_id = file.readline().strip()
        full_url = f"{base_url}{get_pet_by_url}{pet_id}"
        response = requests.get(full_url)
        print(response)
        status_code = response.status_code
        # body = response.json()
        assert status_code == 201, f"Unexpected status code. Expect: {201}, Actual: {status_code}"
