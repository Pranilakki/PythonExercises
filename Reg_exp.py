# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 14:11:00 2019

@author: prani
"""

   total = raw_input('What is the total amount for your online shopping?')
   country = raw_input('Shipping within the US or Canada?')
   
   if country == "US":
       if total <= "50":
           print "Shipping Costs $6.00"
       elif total <= "100":
           print "Shipping Costs $9.00"
       elif total <= "150":
           print "Shipping Costs $12.00"
       else:
           print "FREE"
    if country == "Canada":
        if total <= "50":
            print "Shipping Costs $8.00"
        elif total <="100":
            print "Shipping Costs $12.00"
        elif total <= "150":
            print "Shipping Costs $15.00"
        else:
            print "FREE