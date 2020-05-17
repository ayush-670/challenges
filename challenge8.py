# -*- coding: utf-8 -*-
"""
Created on Sat May 16 23:15:05 2020

@author: Ayush Singh
"""

def timeConversion(s):
    d=s.split(':')
    g=d[0]
    print(g)
    e=d[2]
   
    f=e[2::]
    print(f)
    h=e[:2]
   
    if(int(d[0]) <=12 and int(d[1])<= 59 and int(h)<= 59):
      if(f=='AM' and g=='12' ):
          g='00'
      elif(f=='PM' and g=='12' ):
          g=g
      elif(f=='PM'):
         g=int(g)+12
      
    print(str(g)+':'+str(d[1])+':'+h)
    #c=s
    # Write your code here.
    #

s = input()

result = timeConversion(s)


   
