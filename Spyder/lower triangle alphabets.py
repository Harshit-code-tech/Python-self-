# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 14:32:04 2021

@author: chetan
"""

n = int(input("Enter a number of n: "))
for i in range(n):
    print(" "*i,end="")
    for j in range(n-i):
        print((chr(65+j)+" "),end="")
    print()