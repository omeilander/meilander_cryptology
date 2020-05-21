# -*- coding: utf-8 -*-
"""
Created on Wed May 20 21:36:03 2020

@author: omeil
"""
from Permutation import Permutation as PP

string = "MATHEMATICS"
perm = [2, 4, 1, 3]

encode = PP(perm)
cipherText = (encode.encode(string))
print(encode.decode(cipherText))