import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


@pytest.fixture
def driver():
    print('\nstart browser for test')
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    print('\nquit browser')
    driver.quit()


@pytest.mark.parametrize('link', ['236895',
                                  '236896',
                                  '236897',
                                  '236898',
                                  '236899',
                                  '236903',
                                  '236904',
                                  '236905'])
def test_find_secret_symbols(driver, link):
    link = f'https://stepik.org/lesson/{link}/step/1'
    driver.get(link)
    answer = str(math.log(int(time.time())))
    text_area = driver.find_element(By.CSS_SELECTOR, '.ember-text-area').send_keys(answer)
    btn = driver.find_element(By.CSS_SELECTOR, '.submit-submission').click()
    hint = driver.find_element(By.CSS_SELECTOR, '.smart-hints__hint').text
    assert hint == 'Correct!', "Success message doesn't match"

