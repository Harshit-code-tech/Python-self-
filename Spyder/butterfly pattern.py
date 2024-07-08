# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 21:44:11 2021

@author: chetan
"""

row = int(input("Enter number of rows (even): "))

n = row//2

print("Generated butterfly pattern is:\n")
# Upper part
for i in range(1,n+1):
    for j in range(1, 2*n+1):
        if j>i and j< 2*n+1-i:
            print("  ", end="")
        else:
            print("* ", end="")
    print()