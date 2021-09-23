from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/execute_script.html'
driver = webdriver.Chrome()
driver.get(link)

try:
    x_value = driver.find_element(By.ID, 'input_value').text


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    answer = calc(x_value)

    input = driver.find_element(By.ID, 'answer').send_keys(answer)
    check = driver.find_element(By.ID, 'robotCheckbox').click()
    radio = driver.find_element(By.ID, 'robotsRule')
    btn = driver.find_element(By.TAG_NAME, 'button')

    driver.execute_script('return arguments[0].scrollIntoView(true);', btn)
    radio.click()
    btn.click()

finally:
    time.sleep(5)
    driver.quit()
