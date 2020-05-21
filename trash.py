# -*- coding: utf-8 -*-
"""
Created on Wed May 20 21:46:10 2020

@author: omeil
"""
import numpy
n=5
string = "ILIKEPIZZAONLYONSUNDAYS"
print((string[:n]))

ar = [0, 0, 0, 0, 0]
key = numpy.array((2, 3, 4, 5, 1))-1
i = 3
for i in range(5):
    ar[key[i]] =  string[i]
    
print (ar)