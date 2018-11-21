# -*- coding:utf-8 -*-
from selenium import webdriver
import os
import time
driver = webdriver.Chrome()
FILE_PATH = 'file:///'+os.path.abspath('file.html')
driver.get(FILE_PATH)

driver.find_element_by_name('file').send_keys("/Users/mqf/log.txt")
time.sleep(2)
driver.quit()