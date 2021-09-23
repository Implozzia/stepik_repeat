from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = 'http://suninjuly.github.io/find_link_text'

try:
    driver = webdriver.Chrome()
    driver.get(link)

    num = str(math.ceil(math.pow(math.pi, math.e)*10000))
    answer = driver.find_element_by_link_text(num).click()

    name_input = driver.find_element(By.NAME, 'first_name')
    name_input.send_keys('Ruslan')

    last_name_input = driver.find_element(By.NAME, 'last_name')
    last_name_input.send_keys('Vafin')

    city_input = driver.find_element(By.CLASS_NAME, 'city')
    city_input.send_keys('Moscow')

    country_input = driver.find_element(By.ID, 'country')
    country_input.send_keys('Russia')

    btn = driver.find_element(By.CLASS_NAME, 'btn')
    btn.click()


finally:
    time.sleep(15)
    driver.quit()



