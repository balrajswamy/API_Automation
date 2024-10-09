import pytest
import requests
import allure


@allure.title("Test Authentication")
@allure.description(
    "This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
def test_testcase1():
    print("Hello world,\tTC1")


def test_testcase2():
    print("Hello world,\tTC2")


@pytest.mark.smoke
def test_testcase3():
    print("Hello world,\tTC3")


@pytest.mark.smoke
def test_verify_sum():
    assert 1 + 1 == 2


@pytest.mark.reg
def test_verify_sub():
    assert 1 - 2 == 0


@pytest.mark.skip(reason="Not Completed!")
def test_verify_multi():
    assert 1 * 5 == 5
