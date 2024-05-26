from  selenium.webdriver.common.by import  By

class LoginpageLoaders:
    # Define locators
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".orangehrm-login-button")


def loginPagelocators():
    return None