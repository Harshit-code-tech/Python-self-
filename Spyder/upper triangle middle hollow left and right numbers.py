# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 15:58:42 2021

@author: chetan
"""

n = int(input("Enter a number of n: "))
for i in range(n):
    print("1 "*(n-i-1),chr(65+i) ,end="")
    if i>=1:
        print(" "*(6*i-3)+chr(65+i) ,end=" 4"*i)
    print()