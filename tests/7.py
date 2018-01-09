import unittest

import time
from selenium import webdriver


class MenuClick(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.url = "http://localhost/litecart/admin"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_menu_click(self):
        driver = self.driver
        driver.get(self.url)
        self.assertEqual("My Store", driver.title)

        username = "admin"
        password = "admin"
        driver.find_element_by_xpath("//INPUT[@type='text']").send_keys(username)
        driver.find_element_by_xpath("//INPUT[@type='password']").send_keys(password)
        driver.find_element_by_xpath("//BUTTON[@type='submit'][text()='Login']").click()
        self.assertEqual("My Store", driver.title)
        time.sleep(2)

        #menu = driver.find_elements_by_css_selector("ul#box-apps-menu > li")
        menu = driver.find_elements_by_css_selector("ul#box-apps-menu li#app-")
        print(menu)
        time.sleep(5)

        for i in menu:
            i.click()
            print(i)
            time.sleep(5)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()