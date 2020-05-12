# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:29:57 2020

@author: Ayush Singh
"""

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    pSum=0
    sSum=0
    for i in range(0,n):
        pSum= pSum+arr[i][i]
    for j in range(0,n):
        sSum= sSum+arr[j][(n-1)-j]
    diff= abs(pSum-sSum)
    return diff

    # Write your code here



n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)
print(result)

