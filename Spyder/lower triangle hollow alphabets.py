# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 15:16:00 2021

@author: chetan
"""

n = int(input("Enter a number of n:"))
for i in range(n):
    print(" "*i,chr(65+i),end="")
    if i!= n-1:
        print(" "*(2*n-2*i-3)+chr(65+i),end="")
    print()