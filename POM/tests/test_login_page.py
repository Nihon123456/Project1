import pytest
from selenium import webdriver
from POM.pages.login_page import LoginPage
from POM.utils.config import  login_url
from  POM.utils.config import BROWSER


@pytest.fixture
def setup():
    if BROWSER=='Chrome' :
        driver=webdriver.Chrome()
    elif BROWSER=='Firefox' :
        driver=webdriver.Firefox()

    driver.get(login_url)

    yield driver
    driver.quit()


def test_login_valid(setup):
    login_page = LoginPage(setup)
    login_page.login("Admin", "admin123")


def test_login_invalid(setup):
    login_page = LoginPage(setup)
    login_page.login("Admin12", "admin1232333")