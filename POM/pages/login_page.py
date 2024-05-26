from POM.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from POM.utils.locators import loginPagelocators


class LoginPage(BasePage):


    # define login actions
    def login(self, username, password):
        self.input_text(*loginpagelocators.USERNAME_INPUT, username)
        self.input_text(*loginpagelocators.PASSWORD_INPUT, password)
        self.click_element(*loginpagelocators.LOGIN_BUTTON)
