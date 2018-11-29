#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

import unittest
import time
class BlogHome(unittest.TestCase):
    u"""博客首页"""
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        url = "https://www.cnblogs.com/yoyoketang/"
        cls.driver.get(url)
        cls.driver.implicitly_wait(20)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01(self):
        #u"""验证元素存在：博客园"""
        """
        locator = ("id","blog_nav_sitehome")
        text = u"博客园"
        result = EC.text_to_be_present_in_element(locator,text)(self.driver)
        self.assertTrue(result)
        """
        result = self.driver.find_element_by_xpath("//*[@id='blog_nav_sitehome']").text
        self.assertEqual(result,u"博客园")

    def test_02(self):
        locator = ("id", "blog_nav_myhome")
        text = u"首页"
        result = EC.text_to_be_present_in_element(locator, text)(self.driver)
        self.assertTrue(result)

    if __name__ == "__main__":
        unittest.main()