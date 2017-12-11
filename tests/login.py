import unittest

import time
from selenium import webdriver


class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.url = "http://localhost/litecart/admin/login.php"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login(self):
        driver = self.driver
        driver.get(self.url)
        self.assertEqual("My Store", driver.title)
        print(driver.title)

        username = "admin"
        password = "admin"
        driver.find_element_by_xpath("//INPUT[@type='text']").send_keys(username)
        driver.find_element_by_xpath("//INPUT[@type='password']").send_keys(password)
        driver.find_element_by_xpath("//BUTTON[@type='submit'][text()='Login']").click()
        self.assertEqual("My Store", driver.title)


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()