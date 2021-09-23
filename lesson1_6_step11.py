from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    driver = webdriver.Chrome()
    driver.get(link)

    input_first_name = driver.find_element(By.CSS_SELECTOR, '.form-control.first:required')
    input_first_name.send_keys('Ruslan')

    input_second_name = driver.find_element(By.CSS_SELECTOR, '.form-control.second:required')
    input_second_name.send_keys('Muffin')

    input_email = driver.find_element(By.CSS_SELECTOR, '.form-control.third:required')
    input_email.send_keys('@mail.ru')

    button = driver.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = driver.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    driver.quit()
