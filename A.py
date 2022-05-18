# -*- coding: utf-8 -*-
"""
Created on Tue May 17 23:33:51 2022

@author: ana karen
"""
from set_up import *
from login import *
from logout import *
from dropdown import *

driver = set_up("firefox")
login("standard_user","secret_sauce",driver)
print("Test A is done!")
driver.close()
