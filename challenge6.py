# -*- coding: utf-8 -*-
"""
Created on Wed May 13 23:13:44 2020

@author: Ayush Singh
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May 13 22:41:34 2020

@author: Ayush Singh
"""

def miniMaxSum(arr):
        minSum=0
        maxSum=0
        arr.sort()
        
        arr1=arr[:-1]
        for i in range (len(arr1)):
            minSum=minSum+arr1[i]
        
        
        arr2=arr[1:]
        for j in range (len(arr2)):
            maxSum=maxSum+arr2[j]
            
            
        print(minSum,maxSum)
          
        
    
            
    
    
arr = list(map(int, input().rstrip().split()))

miniMaxSum(arr)
