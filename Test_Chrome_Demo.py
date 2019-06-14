#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://baidu.com")

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()



driver.quit()




