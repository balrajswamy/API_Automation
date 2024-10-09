import pytest
import requests
import allure


@allure.title("Test GET Request - RESTFUL Booker Project#1")
@allure.description("TC#1 Verify that GET Request works with ID")
@allure.tag("regression","p0","smoke")
@allure.label("owner", "Balraj")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_request_by_id_positive():
    url = "https://restful-booker.herokuapp.com/booking/1"
    responseData = requests.get(url)
    print("responseData:\n", responseData.text)

    print("responseData Json:\n", responseData.json())
    print("responseData Headers:\n", responseData.headers)
    assert responseData.status_code == 200

@allure.title("Test GET Request - RESTFUL Booker Project#2")
@allure.description("TC#2 Verify that GET Request works with ID as -1")
@allure.tag("regression","p0","smoke")
@allure.label("owner", "Balraj")
@allure.testcase("TC#2")
@pytest.mark.smoke
def test_get_single_request_by_id_negative1():
    url = "https://restful-booker.herokuapp.com/booking/-1"
    responseData = requests.get(url)
    print("responseData:\n", responseData.text)

    print("responseData Json:\n", responseData.json())
    print("responseData Headers:\n", responseData.headers)
    assert responseData.status_code == 404

@allure.title("Test GET Request - RESTFUL Booker Project#3")
@allure.description("TC#3 Verify that GET Request works with ID as invalid")
@allure.tag("regression","p0","smoke")
@allure.label("owner", "Balraj")
@allure.testcase("TC#3")
@pytest.mark.smoke
def test_get_single_request_by_id_negative():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    responseData = requests.get(url)
    print("responseData:\n", responseData.text)

    print("responseData Json:\n", responseData.json())
    print("responseData Headers:\n", responseData.headers)
    assert responseData.status_code == 404