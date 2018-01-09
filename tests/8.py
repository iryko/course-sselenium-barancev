import unittest

import time
from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException


class StickerPresence(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.url = "http://localhost/litecart/en/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_menu_click(self):
        driver = self.driver
        driver.get(self.url)
        self.assertEqual("Online Store | My Store", driver.title)
        section = driver.find_elements_by_css_selector("div#box-most-popular ul li")
        try:
            for i in section:
                if len(i.find_elements_by_class_name('sticker')) == 1:
                    print("one image- one sticker")
        except Exception as e:
            print(e)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()