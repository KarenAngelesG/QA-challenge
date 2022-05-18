# -*- coding: utf-8 -*-
"""
Created on Tue May 17 22:46:00 2022

@author: ana karen
"""
from set_up import *
from login import *
from logout import *

driver = set_up("firefox")
login("invalid_user","secret_sauce",driver)