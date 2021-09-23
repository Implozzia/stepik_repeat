from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = 'http://suninjuly.github.io/math.html'
driver = webdriver.Chrome()
driver.get(link)

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_value = driver.find_element(By.ID, 'input_value').text

    answer = calc(x_value)

    input = driver.find_element(By.ID, 'answer')
    input.send_keys(answer)

    checkbox = driver.find_element(By.ID, 'robotCheckbox').click()
    radio = driver.find_element(By.ID, 'robotsRule').click()

    btn = driver.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(10)
    driver.quit()
