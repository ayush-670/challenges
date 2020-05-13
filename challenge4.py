# -*- coding: utf-8 -*-
"""
Created on Wed May 13 18:39:07 2020

@author: Ayush Singh
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice=0
    bob=0
    arr=[]
    if(len(a)==len(b)):
     for i in range(len(a)):
        if(a[i]>b[i]):
            alice=alice+1
        elif(a[i]<b[i]):
            bob=bob+1
        else:
            print('',end=" ")
    else:
        print("list length not same")
        
    arr=[alice,bob]
    return arr
        
    
        


a = list(map(int, input().rstrip().split()))

b = list(map(int, input().rstrip().split()))

result = compareTriplets(a, b)

print(result)
