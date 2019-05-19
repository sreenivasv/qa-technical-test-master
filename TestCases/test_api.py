import requests
import json

BASE_URL = "http://localhost:5000/v1"


def test_get_productlist():
    # Relative URL For GET
    productList_URL = "/products"

    # Make GET Request
    response = requests.get(BASE_URL + productList_URL)

    # Validating Response Code
    assert response.status_code == 200


def test_creat_new_product():
    # Relative URL For POST
    creatProduct_URL = "/product"

    # Read input Json file
    file = open(
        'C:\\Users\\Thinkpad\\Downloads\\qa-technical-test-latest\\qa-technical-test-master\\TestCases\\postData.json',
        'r')
    json_input = file.read()
    request_json = json.loads(json_input)

    # Make Post Request with Json input body
    response = requests.post(BASE_URL + creatProduct_URL, request_json)

    # Validating Response Code
    assert response.status_code == 200

