from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/huge_form.html")
    elements = driver.find_elements(By.TAG_NAME, 'input')
    for element in elements:
        element.send_keys('click')

    button = driver.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    driver.quit()
