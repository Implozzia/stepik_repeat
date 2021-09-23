from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


link = 'http://suninjuly.github.io/selects1.html'
driver = webdriver.Chrome()
driver.get(link)


try:
    first_num = int(driver.find_element(By.ID, 'num1').text)
    second_num = int(driver.find_element(By.ID, 'num2').text)
    sum = first_num + second_num

    select = Select(driver.find_element(By.ID, 'dropdown'))
    select.select_by_value(str(sum))

    btn = driver.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(3)
    driver.quit()
