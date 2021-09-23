import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


link = 'http://suninjuly.github.io/explicit_wait2.html'
driver = webdriver.Chrome()
driver.get(link)

try:
    price = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    btn = driver.find_element(By.ID, 'book').click()

    x_value = driver.find_element(By.ID, 'input_value').text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    answer = calc(x_value)
    answer_inout = driver.find_element(By.ID, 'answer').send_keys(answer)
    submit_btn = driver.find_element(By.ID, 'solve')
    driver.execute_script('return arguments[0].scrollIntoView(true);', submit_btn)
    submit_btn.click()

finally:
    time.sleep(5)
    driver.quit()




