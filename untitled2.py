# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:20:47 2019

@author: prani
"""

username = raw_input("Enter your name :")
print ("Hello " + username)

temperature_farheinit = raw_input("Enter Fahrenhit temperature :")
temperature_celsius = (float(temperature_farheinit) - 32) * 5/9
print temperature_celsius


Hours= raw_input("Enter Hours:")
Rate = raw_input("Enter Rate :")
Gross_Pay = float(Hours) * float(Rate)
print Gross_Pay

 a = [4,7,3,2,5,9]
for i in a:
     print ("Element " + str(i) + " Index is .." + str(a.index(i)))
     

my_map = { 'a' : 1, 'b' : 2}
inv_map = { v : k for k,v in my_map.iteritems()}
print inv_map

list= [ 'a', 'b', 'c', 'd']
Dict = { i : list[i] for i in range(1 ,len(list))}
print Dict