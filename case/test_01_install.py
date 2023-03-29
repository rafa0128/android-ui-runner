# coding: utf-8
# author: Rafa Chen
# modified by : Rafa Chen
# modification time: 2023-3-28

from public.Decorator import *
from public.Common import Driver
from public.BasePage import *
from logzero import logger
import unittest

d = Driver()

class Install(unittest.TestCase):
    
    @classmethod
    @setupclass(d)
    def setUpClass(cls):
        d.driver.app_stop_all()
        d.driver.screen_on() # 打开屏幕
        d.driver.unlock() # 解锁屏幕
        d.driver.press('home') # 回到桌面


    @classmethod
    @teardownclass(d)
    def tearDownClass(cls):
        # d.driver.app_stop(d.pkgname)
        pass

    @testcase(d)
    def test_01_install(self):
        """卸载安装"""
        d.driver.app_uninstall(d.pkgname)
        d.driver.app_install(d.apk_path)

    @testcase(d)
    def test_02_startup(self):
        """启动app"""
        d.driver.app_start(d.pkgname)
        Action.exist_click(Elements.text, '继续')
        Action.exist_click(Elements.text, '确定')
        self.assertTrue(d.driver(text="Login").exists(timeout=10), msg='没有发现启动成功页面')
        d.screenshot('startup')

    @testcase(d)
    def test_03_login(self):
        """登录"""
        d.driver(resourceId='com.github.android_app_bootstrap:id/mobileNoEditText').click()
        d.driver.send_keys('123')
        d.driver(resourceId='com.github.android_app_bootstrap:id/codeEditText').click()
        d.driver.send_keys('456')
        d.driver(resourceId='com.github.android_app_bootstrap:id/login_button').click()
        self.assertTrue(d.driver(resourceId="com.github.android_app_bootstrap:id/list_button").exists(timeout=10))
        d.screenshot('login')
