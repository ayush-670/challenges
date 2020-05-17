# -*- coding: utf-8 -*-
"""
Created on Sun May 17 11:38:39 2020

@author: Ayush Singh
"""


# Complete the superReducedString function below.
def superReducedString(s):
    LS = list(s)
    i = 0 
    while i < len(LS)-1:
        if LS[i]==LS[i+1]:
            del LS[i]
            del LS[i]
            i = 0
            if len(LS) == 0:
                print ('Empty String')
                break
        else:
            i+=1
    if(len(LS)== 0 ):
        return 'Empty String'
    else:
        return ''.join(LS)




s = input()

result = superReducedString(s)

