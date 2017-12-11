import unittest
from selenium import webdriver


class GetPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.url = "https://www.google.it/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_get_url(self):
        driver = self.driver
        driver.get(self.url)
        self.assertEqual("Google", driver.title)


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()