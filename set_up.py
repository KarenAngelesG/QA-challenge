# -*- coding: utf-8 -*-
"""
Created on Tue May 17 21:10:58 2022

@author: ana karen
"""
from selenium import webdriver

def set_up(browser):
    if browser == "chrome":
        from webdriver_manager.chrome import ChromeDriverManager
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser == "firefox":
        from webdriver_manager.firefox import GeckoDriverManager
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser== "edge":
        from webdriver_manager.microsoft import EdgeChromiumDriverManager
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    return driver

