# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 21:09:16 2020

@author: omeil
"""
from IOC import IOC

class Vigenere (object):
    def __init__(slef, key):
        slef.key = []
        for i in range(len(key)):
            slef.key.append(ord(key[i]) - 65)
            
    def encode(slef, S):
        Snum = []
        new = ""
        for i in range(len(S)):
            Snum.append(ord(S[i]) - 65)
            Snum[i] += slef.key[i % len(slef.key)]
            ch = chr((Snum[i] % 26) + 65)
            new += ch
        
        return(new)
        
    def decode(slef, S):
        Snum = []
        new = ""
        for i in range(len(S)):
            Snum.append(ord(S[i]) - 65)
            Snum[i] -= slef.key[i % len(slef.key)]
            ch = chr((Snum[i] % 26) + 65)
            new += ch
        
        return(new)
        
def findL(S):
    n = len(S)
    IoC = IOC(S)
    ioc = IoC.calcIOC()
    ill = (0.027 * n) / ((ioc * (n - 1)) + 0.065 - (0.038 * n))
    if (ill == 0):
        ill = 1
    return ((ill))
        
        
        
