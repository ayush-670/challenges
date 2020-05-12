# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:54:36 2020

@author: Ayush Singh
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive=0
    negative=0
    nonzero=0
    for i in arr:
        if(i>0):
            positive=positive+1
        elif(i<0):
            negative=negative+1
        else:
            nonzero=nonzero+1
    positive_ratio=positive/n
    print("{:.6f}".format(positive_ratio))
    negative_ratio=negative/n
    print("{:.6f}".format(negative_ratio))
    nonzero_ratio=nonzero/n
    print("{:.6f}".format(nonzero_ratio))
    
    
    


n = int(input())

arr = list(map(int, input().rstrip().split()))

plusMinus(arr)
