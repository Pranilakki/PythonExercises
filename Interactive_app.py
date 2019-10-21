# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 14:06:04 2019

@author: prani
"""

str='www.edureka.com'
lst_str = str.split('.')
print(lst_str[0].replace('w','')+lst_str[1]+lst_str[2].replace('w',''))