# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 14:27:05 2020

@author: omeil
"""

class Hill(object):
    
    def __init__(self, k1, k2, k3, k4):
        self.k1 = k1
        self.k2 = k2
        self.k3 = k3
        self.k4 = k4
        self.d = ((self.k1 * self.k4) - (self.k2 * self.k3)) % 26
        self.inv = self._getInv(self.d)
        
    def gcd(self):
        a = self.d
        b = 26
        
        while(b != 0):
            a = b
            b = a%b
            
        return a
    
    def encode(self, string):
        newS = ""
        if ((len(string) % 2) == 1):
            string += 'X'
        
        for i in range(int(len(string) / 2)):
            ch1 = string[(2*i)]
            ch2 = string[(2*i) + 1]
            C1 = (self.k1 * (ord(ch1) - 65) + self.k2 * (ord(ch2) - 65)) % 26
            C2 = (self.k3 * (ord(ch1) - 65) + self.k4 * (ord(ch2) - 65)) % 26
            
            ch1 = chr(C1 + 65)
            ch2 = chr(C2 + 65)
            newS += ch1
            newS += ch2
        
        return newS
    
    def _encodedc(self, string, k1, k2, k3, k4):
        newS = ""
        if ((len(string) % 2) == 1):
            string += 'X'
        
        for i in range(int(len(string) / 2)):
            ch1 = string[(2*i)]
            ch2 = string[(2*i) + 1]
            C1 = (k1 * (ord(ch1) - 65) + k2 * (ord(ch2) - 65)) % 26
            C2 = (k3 * (ord(ch1) - 65) + k4 * (ord(ch2) - 65)) % 26
            
            ch1 = chr(C1 + 65)
            ch2 = chr(C2 + 65)
            newS += ch1
            newS += ch2
        
        return newS
        
    def decode(self, string):
        newk1 = (self.k4 * self.inv) % 26
        newk2 = (-self.k2 * self.inv) % 26
        newk3 = (-self.k3 * self.inv) % 26
        newk4 = (self.k1 * self.inv) % 26
        return(self._encodedc(string, newk1, newk2, newk3, newk4))
        
    
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
        
        
        
        
        
        
