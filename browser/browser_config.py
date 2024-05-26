from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://www.google.com")
time.sleep(10)
driver.close()

driver=webdriver.Firefox()
driver.get("https://www.google.com")

