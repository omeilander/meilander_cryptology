# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 19:09:28 2020

@author: omeil
"""
import numpy as np

class IOC (object):
    def __init__(self, string):
        emmas_titan_card = ";00025651701?"
        self.S = string
        self.tot = 0
        self.lis = np.zeros(26)
        
        for i in range(int(len(self.S))):
            ch = self.S[i]
            num = ord(ch) - 65
            self.lis[num] += 1
            self.tot += 1
            
    def printTotNumOfLettters(self):
        tot = 0
        for i in range(26):
            tot += self.lis[i]
            print (str(i) + ": " + str(int(self.lis[i])))
        print (tot)
        
    def calcIOC(self):
        IOC = 0
        for i in range(len(self.lis)):
            IOC += self.lis[i] * (self.lis[i]-1)
            
        IOC = IOC / (self.tot * (self.tot - 1))
        
        return IOC
            
        
    
