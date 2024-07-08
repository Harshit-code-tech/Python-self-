# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 13:08:28 2021

@author: chetan
"""

n = int(input("Enter a number of n:"))
for i in range(n):
    print(" "*(n-i-1),end="")
    for j in range(i+1):
        print(j+1,end="")
    print()
for i in range(n-1):
    print(" "*(i+1),end="")
    for j in range(n-i-1):
        print(j+1,end="")
    print()