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
        
    def _reset(self):
        self.new = ""
        self.lis = np.zeros(26)
        
    def encode(self, planeText, numLetters = True):
        self._reset()
        self.numLetters = numLetters 
    
        for i in range(len(planeText)):
            ch = planeText[i]
            num = ord(ch) - 65
            self.lis[num] += 1
        
            num = (self.m * num + self.n) % 26
            ch = chr(num + 65)
            self.new += ch
        print(self.new)
        print()
            
        if (numLetters == True):
            self._numLet()
        return (self.new)
    
    def _numLet(self):
        for i in range(26):
            print (str(i) + ": " + str(int(self.lis[i])))




            
    def decode(self, cipherText):
        """im going to try my best"""
        
        return(self._encodedc(cipherText, self._getInv(self.m), 26 - self.n))


        
    def _encodedc(self, cipherText, m, n):
        self._reset()
    
        for i in range(len(cipherText)):
            ch = cipherText[i]
            num = ord(ch) - 65
            self.lis[num] += 1
        
            num = (m * num + n) % 26
            ch = chr(num + 65)
            self.new += ch
        print(self.new)
        print()
            
        return (self.new)

    def _getInv(self, d):
        if (d == 1):
            return(1)
        elif (d == 3):
            return(9)
        elif (d == 5):
            return(21)
        elif (d == 7):
            return(15)
        elif (d == 9):
            return(3)
        elif (d == 11):
            return(19)
        elif (d == 15):
            return(7)
        elif (d == 17):
            return(23)
        elif (d == 19):
            return(11)
        elif (d == 21):
            return(5)
        elif (d == 23):
            return(17)
        elif (d == 25):
            return(25)




            
    def encodefs(self, S, fs = True):
        self._reset()
        self.fs = fs 
    
        for i in range(len(S)):
            ch = S[i]
            num = ord(ch) - 65
            self.lis[num] += 1
        
            num = (self.m * num + self.n) % 26
            ch = chr(num + 65)
            self.new += ch
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


   
