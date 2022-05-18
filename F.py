# -*- coding: utf-8 -*-
"""
Created on Tue May 17 23:37:04 2022

@author: ana karen
"""
from set_up import *
from login import *
from logout import *
from dropdown import *
from purchase import *
from onesie import *

driver = set_up("firefox")
login("standard_user","secret_sauce",driver)
onesie(driver)
