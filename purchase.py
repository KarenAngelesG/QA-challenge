# -*- coding: utf-8 -*-
"""
Created on Tue May 17 23:25:28 2022

@author: ana karen
"""

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

def purchase(driver):
    url1 = "https://www.saucedemo.com/"
    url2 = "https://www.saucedemo.com/inventory.html"
    url3 = "https://www.saucedemo.com/cart.html"
    url4 = "https://www.saucedemo.com/checkout-step-one.html"
    url5 = "https://www.saucedemo.com/checkout-step-two.html"
    url6 = "https://www.saucedemo.com/checkout-complete.html"
    finaltext = "THANK YOU FOR YOUR ORDER"
    
    addcarBtn = driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-onesie"]')
    addcarBtn.click()
    carBtn = driver.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a')
    carBtn.click()
    curl = driver.current_url
    assert (url3 == curl)
    time.sleep(3)
     
    CheckBtn = driver.find_element(By.XPATH,'//*[@id="checkout"]')
    CheckBtn.click()
    curl = driver.current_url
    assert (url4 == curl)
    time.sleep(3)
    
    FrstNameBtn = driver.find_element(By.XPATH,'//*[@id="first-name"]')
    FrstNameBtn.send_keys("Karen")
    LstNameBtn = driver.find_element(By.XPATH,'//*[@id="last-name"]')
    LstNameBtn.send_keys("Angeles")
    PCBtn = driver.find_element(By.XPATH,'//*[@id="postal-code"]')
    PCBtn.send_keys("07300")
    CntBtn = driver.find_element(By.XPATH,'//*[@id="continue"]')
    CntBtn.click()
    curl = driver.current_url
    assert (url5== curl)
    time.sleep(3)
    
    
    FnshBtn = driver.find_element(By.XPATH,'//*[@id="finish"]')
    FnshBtn.click()
    time.sleep(3)

    curl = driver.current_url
    assert (url6== curl)
    
    FinishPage = driver.find_element(By.XPATH,'//*[@id="checkout_complete_container"]/h2')
    finishtext = FinishPage.text
    
    assert (finaltext == finishtext)
    print("Test G is done!")
