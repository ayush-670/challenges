# -*- coding: utf-8 -*-
"""
Created on Wed May 13 21:34:33 2020

@author: Ayush Singh
"""

def aVeryBigSum(ar):
    sum=0
    for i in range(len(ar)):
        sum=sum+ar[i]
    return sum

ar_count = int(input())

ar = list(map(int, input().rstrip().split()))

result = aVeryBigSum(ar)
print(result)