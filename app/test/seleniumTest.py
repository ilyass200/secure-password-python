import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def generic_selenium_test(taille, boxCheck, hashAlgorithm):
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8080/")

    password_length_field = driver.find_element(By.NAME, "password_length")
    password_length_field.send_keys(taille)

    include_checkbox = driver.find_element(By.NAME, boxCheck)
    include_checkbox.click()
    time.sleep(2)
    generate_button = driver.find_element(By.NAME, "btn_generer")
    generate_button.click()
    time.sleep(2)

    hash_function = Select(driver.find_element(By.NAME, "include_hash"))
    hash_function.select_by_value(hashAlgorithm)
    time.sleep(2)
    hash_button = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, "btn_hash"))
    )
    hash_button.click()
    time.sleep(3)

    driver.quit()


if __name__ == '__main__':
    generic_selenium_test(5, "include_numbers", "md5")
    generic_selenium_test(16, "include_symbols", "sha256")
    generic_selenium_test(18, "include_symbols", "")
