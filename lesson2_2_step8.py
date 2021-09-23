from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = 'http://suninjuly.github.io/file_input.html'
driver = webdriver.Chrome()
driver.get(link)

try:
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = 'step8.txt'
    file_path = os.path.join(current_dir, file_name)

    first_name_input = driver.find_element(By.NAME, 'firstname').send_keys('Ruslan')
    second_name_input = driver.find_element(By.NAME, 'lastname').send_keys('Muffin')
    email = driver.find_element(By.NAME, 'email').send_keys('@mail.ru')
    file_upload = driver.find_element(By.ID, 'file').send_keys(file_path)
    btn = driver.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(5)
    driver.quit()

