import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.locators import LoginPageLocators

# configure the logging settings
logging.basicConfig(filename="test_log.log", level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

screenshot_file_path = "E:\\python\\pythonProject\\screencap"


def login_testCase1_valid():

    logging.info('login_testCase1_valid Execution Start....')
    # Step 1: Launch Browser
    driver = webdriver.Firefox()
    logging.info('Firefox Launch Successful.')
    driver.maximize_window()
    driver.implicitly_wait(5)

    # Step 2: Open URL
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    logging.info('Login pages open Successful.')

    # Step 3: Enter Username
    username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.username_field))
    username_field_enable_state = username_field.is_enabled()

    # verify username field is enabled or nor
    if username_field_enable_state:
        username_field.clear()
        username_field.send_keys("Admin")
        logging.info('Type Username Successful.')
    else:
        logging.error("Username field is not enabled.Test Failed.")

    # Step 4: Enter Password
    password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.password_field))
    password_field_enable_state = password_field.is_enabled()

    # verify password field is enabled or not
    if password_field_enable_state:
        password_field.clear()
        password_field.send_keys("admin123")
        logging.info('Type Password Successful.')
    else:
        logging.error("Password field is not enabled.Test Failed")

    # Step 5: Click Login button
    login_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.login_button))
    login_button.click()
    logging.info('Login Button clicked Successful.')
    time.sleep(5)

    # verify login or not by check URL
    expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    actual_url = driver.current_url

    if expected_url == actual_url:
        logging.info('Test Passed. Login successful.')
        # capture screenshot
        driver.get_screenshot_as_file(screenshot_file_path+"\\login_passed_test_passed.png")
    else:
        logging.error("Test Failed. Login failed.")
        # capture screenshot
        driver.get_screenshot_as_file(screenshot_file_path+"\\login_failed_test_failed.png")

    driver.close()
    logging.info('login_testCase1_valid execution completed..')


def login_testCase2_invalid():
    logging.info('login_testCase2_invalid Execution Start....')
    # Step 1: Launch Browser
    driver = webdriver.Firefox()
    logging.info('Firefox Launch Successful.')
    driver.maximize_window()

    # Step 2: Open URL
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


    # Step 3: Enter Username
    username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "username")))
    username_field_enable_state = username_field.is_enabled()

    # verify that username field is enabled or not
    if username_field_enable_state:
        username_field.clear()
        username_field.send_keys("Admin123")
        logging.info('Type Username Successful.')
    else:
        logging.error("Username field is not enabled.Test Failed.")

    # Step 4: Enter Password
    password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
    password_field_enable_state = password_field.is_enabled()

    # verify that password field is enabled or not
    if password_field_enable_state:
        password_field.clear()
        password_field.send_keys("admin123")
        logging.info('Type Password Successful.')
    else:
        logging.error("Password field is not enabled.Test Failed")

    # Step 5: Click Login button
    login_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".orangehrm-login-button")))
    login_button.click()
    logging.info('Login Button clicked Successful.')
    time.sleep(4)

    # verify login or not by check error message
    error_message = driver.find_element(By.CSS_SELECTOR, ".oxd-alert-content-text")
    actual_error_message_text = error_message.text

    expected_error_message = "Invalid credentials"

    if expected_error_message == actual_error_message_text:
        logging.info("Test Passed. Login failed.Error message: " + expected_error_message)
        # capture screenshot
        driver.get_screenshot_as_file(screenshot_file_path + "\\test_passed_login_failed.png")
    else:
        logging.error("Test Failed. Did not get expected error message: " + expected_error_message)
        driver.get_screenshot_as_file(screenshot_file_path + "\\test_failed_login_passed.png")

    driver.close()
    logging.info('login_testCase2_invalid execution completed..')


login_testCase1_valid()
# login_testCase2_invalid()