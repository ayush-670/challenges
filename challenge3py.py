# -*- coding: utf-8 -*-
"""
Created on Tue May 12 23:31:39 2020

@author: Ayush Singh
"""
def staircase(n):
 for i in range(1, n + 1):
       print(' ' * (n - i) + '#' * i)

if __name__ == '__main__':
    n = int(input())

    staircase(n)


