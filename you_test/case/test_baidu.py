#coding:utf-8
import unittest
import time.sleep
from selenium import webdriver
class Test_baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.sleep(3)
        self.url = "https://baidu.com"
    def tearDown(self):
        self.driver.quit()
    def test_query(self):
        driver = self.driver
        driver.get(self.url)
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
        time.sleep(3)
        driver.quit()

if __name__ == "__main__":
    unittest.main()