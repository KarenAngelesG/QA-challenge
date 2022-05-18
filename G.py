# -*- coding: utf-8 -*-
"""
Created on Tue May 17 23:23:09 2022

@author: ana karen
"""
from set_up import *
from login import *
from logout import *
from dropdown import *
from purchase import *

driver = set_up("firefox")
login("standard_user","secret_sauce",driver)
purchase(driver)
driver.close()