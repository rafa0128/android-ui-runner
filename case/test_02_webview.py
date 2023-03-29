# coding: utf-8
# author: Rafa Chen
# modified by : Rafa Chen
# modification time: 2023-3-28

from public.Decorator import *
from public.Common import Driver
from selenium.webdriver.common.by import By
from public.chromedriver import *
from logzero import logger
import unittest

d = Driver()

class Webview(unittest.TestCase):
    
    @testcase(d)
    def test_01_baidu(self):
        d.driver(text='Baidu').click(timeout=5)
        self.assertTrue(d.driver(text="百度一下,你就知道").exists(timeout=10))
        dri = ChromeDriver(d.driver, 3456).driver() # 要先配置chromedriver到环境变量中, 翻墙网络
        dri.find_element(By.ID, 'index-kw').send_keys('python')
        dri.find_element(By.ID, 'index-bn').click()
        dri.quit()
        ChromeDriver.kill()
        d.screenshot('baidu')