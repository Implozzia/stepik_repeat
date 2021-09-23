from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = 'http://suninjuly.github.io/alert_accept.html'
driver = webdriver.Chrome()
driver.get(link)

try:
    btn = driver.find_element(By.TAG_NAME, 'button').click()
    confirm = driver.switch_to.alert
    confirm.accept()
    x_value = driver.find_element(By.ID, 'input_value').text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    answer = calc(x_value)
    answer_inout = driver.find_element(By.ID, 'answer').send_keys(answer)
    submit_btn = driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()

finally:
    time.sleep(5)
    driver.quit()


