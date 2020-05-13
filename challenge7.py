# -*- coding: utf-8 -*-
"""
Created on Wed May 13 23:48:17 2020

@author: Ayush Singh
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May 13 23:28:26 2020

@author: Ayush Singh
"""

def birthdayCakeCandles(ar):
    tallest=max(ar)
    k=0
    print(tallest)
    for i in ar:
        if(i==tallest):
         k=k+1
    print(k)
    




ar_count = int(input())

ar = list(map(int, input().rstrip().split()))

result = birthdayCakeCandles(ar)

   
