# -*- coding: utf-8 -*-
"""
Created on Tue May 17 23:37:27 2022

@author: ana karen
"""
from selenium.webdriver.common.by import By
import time
url1 = "https://www.saucedemo.com/"
url2 = "https://www.saucedemo.com/inventory.html"
url3 = "https://www.saucedemo.com/cart.html"
url4 = "https://www.saucedemo.com/checkout-step-one.html"
url5 = "https://www.saucedemo.com/checkout-step-two.html"
url6 = "https://www.saucedemo.com/checkout-complete.html"
finaltext = "Sauce Labs Onesie"

def onesie(driver):
        
    addcarBtn = driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-onesie"]')
    addcarBtn.click()
    carBtn = driver.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a')
    carBtn.click()
    curl = driver.current_url
    assert (url3 == curl)
    time.sleep(3)
     
    FinishPage = driver.find_element(By.CLASS_NAME,"inventory_item_name")
    finishtext = FinishPage.text
    print(finishtext)
    assert (finaltext == finishtext)
    
    
    print("Test F is done!")
    
    driver.close()
