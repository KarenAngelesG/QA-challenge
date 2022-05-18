# -*- coding: utf-8 -*-
"""
Created on Wed May 18 00:43:55 2022

@author: ana karen
"""

from set_up import *
from login import *
from items import *

driver = set_up("firefox")
login("standard_user","secret_sauce",driver)
items(driver)