# -*- coding: utf-8 -*-
"""
Created on Sun May 17 11:05:09 2020

@author: Ayush Singh
"""

def superReducedString(s):
    stack = []
    if  s:
     for c in s:
        if stack and c == stack[-1]:
            stack.pop()
        else:
            stack.append(c)
     else:
         print("Empty String")

    return ''.join(stack)


s = input()
result = superReducedString(s)
print(result)