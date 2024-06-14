# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 15:14:49 2021

@author: chetan
"""

price=float(input("Enter Price : "))
dp=float(input("Enter discount % : "))
discount=price*dp/100 
sp=price-discount
print("Cost Price : ",price)
print("Discount: ",discount)
print("Selling Price : ",sp)
