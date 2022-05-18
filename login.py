# -*- coding: utf-8 -*-
"""
Created on Tue May 17 22:05:01 2022

@author: ana karen
"""
import time

def login(user,password,driver):
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    time.sleep(1)
    
    userid = driver.find_element_by_id("user-name")
    userid.send_keys(user)
    
    passid = driver.find_element_by_id("password")
    passid.send_keys(password)
    
    time.sleep(1)
    
    login = driver.find_element_by_id("login-button")
    login.click()
    time.sleep(1)
    
    url = "https://www.saucedemo.com/inventory.html"
    curl = driver.current_url
    
    assert (url == curl)