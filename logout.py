# -*- coding: utf-8 -*-
"""
Created on Tue May 17 22:05:56 2022

@author: ana karen
"""
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

def logout(driver):

    menu = driver.find_element_by_id("react-burger-menu-btn")
    menu.click()
    
    driver.find_element_by_id("logout_sidebar_link").click()

    nurl = "https://www.saucedemo.com/"
    ncurl = driver.current_url
    time.sleep(1)
    
    driver.close()
    
    assert (nurl == ncurl)    