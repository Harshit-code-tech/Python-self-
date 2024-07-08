# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 21:55:04 2021

@author: chetan
"""

s=input("Enter string:")
vowels=0
for i in s:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
print("Number of vowels are:")
print(vowels)
if vowels == 0:
    print('No vowels found')
else:
    print('Total vowels are :' + str(vowels))