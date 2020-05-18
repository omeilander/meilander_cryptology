# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 14:06:47 2020

@author: omeil
"""
import numpy as np


S = "SECRETMESSAGE"
m = 3
n = 7
class Affine(object):
    def __init__ (self, m, n):
        self.m = m
        self.n = n
        
    def reset(self):
        self.new = ""
        self.lis = np.zeros(26)
        
    def encode(self, S, numLetters = True):
        self.reset()
        self.numLetters = numLetters 
        #print(S)
    
        for i in range(len(S)):
            ch = S[i]
            num = ord(ch) - 65
            self.lis[num] += 1
        
            num = (self.m * num + self.n) % 26
            ch = chr(num + 65)
            self.new += ch
#        if (self.new[0] == 'H' and self.new[1] == "E" and self.new[2] == 'H'):
        print(self.new)
        print()
            
        if (numLetters == True):
            self.numLet()
        return (self.new)
    
    def numLet(self):
        for i in range(26):
            print (str(i) + ": " + str(int(self.lis[i])))
            
    def encodefs(self, S, fs = True):
        self.reset()
        self.fs = fs 
        #print(S)
    
        for i in range(len(S)):
            ch = S[i]
            num = ord(ch) - 65
            self.lis[num] += 1
        
            num = (self.m * num + self.n) % 26
            ch = chr(num + 65)
            self.new += ch
#        if (self.new[0] == 'H' and self.new[1] == "E" and self.new[2] == 'H'):
        print(self.new)
        print()
            
        if (fs == True):
            self.frequencySum()
        return (self.new)
            
    def frequencySum(self):
        fqt = np.empty(26)
        f= np.array((.081, .015, .022, .043, .127, .022, .020, .061, .070, .002, .013, .040, .024, .067, .075, .019, .001, .060, .063, .094, .028, .010, .026, .002, .020, .001, .081, .015, .022, .043, .127, .022, .020, .061, .070, .002, .013, .040, .024, .067, .075, .019, .001, .060, .063, .094, .028, .010, .026, .002, .020, .001))
        for i in range(26):
            sum = 0
            for j in range(len(self.lis)):
                sum += self.lis[j] * f[i + j]
                
            fqt[i] = sum
            
        for i in range(26):
            print (str(i) + ": " + str(fqt[i]))


   