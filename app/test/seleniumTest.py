import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # replace with the appropriate driver for your browser

# Use the get() method to load the webpage:
driver.get("http://127.0.0.1:8080/")

password_length_field = driver.find_element(By.NAME, "password_length")
password_length_field.send_keys("8")

include_numbers_checkbox = driver.find_element(By.NAME, "include_numbers")
include_numbers_checkbox.click()
time.sleep(2)
generate_button = driver.find_element(By.XPATH, "//input[@type='submit']")
generate_button.click()

password_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//p[@id='generated-password']"))
)
password = password_element.text
time.sleep(2)
hash_button = driver.find_element(By.XPATH, "//button[@id='hash-button']")
hash_button.click()

hashed_password_element = driver.find_element(By.XPATH, "//p[@id='hashed-password']")
hashed_password = hashed_password_element.text

driver.quit()
