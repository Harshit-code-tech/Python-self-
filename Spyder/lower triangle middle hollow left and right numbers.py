# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 15:08:05 2021

@author: chetan
"""

n = int(input("Enter a number of n:"))
for i in range(n):
    print("1 "*i,chr(65+i),end="")
    if i!= n-1:
        print(" "*(3*n-3*i-3)+chr(65+i),end=" 4"*i)
    print()