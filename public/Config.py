#!/usr/bin/env python
# -*- coding: utf-8 -*-
import configparser
import os


BATH_DIR = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(BATH_DIR, "config.ini")

class ReadConfig:

    cf = configparser.ConfigParser()
    cf.read(configPath, encoding='UTF-8')

    @classmethod
    def get_pkgname(cls):
        value = cls.cf.get("APP", 'package_name')
        return value
    
    @classmethod
    def get_apk_path(cls):
        value = cls.cf.get("PATH", 'apk')
        path = os.path.join(os.getcwd(), 'apk', value)
        return path