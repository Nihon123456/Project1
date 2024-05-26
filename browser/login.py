import time

from selenium import webdriver
from selenium.webdriver.common.by import By


#def login_test_valid():

driver = webdriver.Firefox()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

username_field = driver.find_element(By.NAME, "username")
username_field.send_keys("Admin")

password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("admin123")

#login_button = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")
#login_button.click()
time.sleep(3)

driver.close()


#login_test_valid()
