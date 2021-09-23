from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest



class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_first_registration(self):
        driver = self.driver
        link = "http://suninjuly.github.io/registration1.html"
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

        self.assertEqual('Congratulations! You have successfully registered!', welcome_text, "Success message "
                                                                                             "doesn't match")

    def test_second_registration(self):
        driver = self.driver
        link = "http://suninjuly.github.io/registration2.html"
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

        self.assertEqual('Congratulations! You have successfully registered!', welcome_text, "Success message "
                                                                                             "doesn't match")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
