# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 14:06:47 2020

@author: omeil
"""

S = "SECRETMESSAGE"
ch = ''
num = 0
lis = ""

print(S)

for i in range(len(S)):
    ch = S[i]
    num = ord(ch) - 65
    
    num = (3 * num + 7) % 26
    ch = chr(num + 65)
    lis = lis+ch
print(lis)
    


   