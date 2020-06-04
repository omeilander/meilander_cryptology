# -*- coding: utf-8 -*-
"""
Created on Wed June 3 19:28:45 2020

@author: omeil
"""
from KCT import KCT

class GedeFu18(object):
    """ """

    def __init__(self, key, setOfEnc = 0):
        self.key = key
        self.KCTob = KCT(key)
        self.soe = setOfEnc
        self.tableCipher = []

        self.tablePlane = ['B', '5', 'X', 'Q', 'J', 'C',
                           '6', 'Y', 'R', 'K', 'D', '7',
                           'Z', 'S', 'L', 'E', '8', '1',
                           'T', 'M', 'F', '9', '2', 'U',
                           'N', 'G', '0', '3', 'V', 'O',
                           'H', 'A', '4', 'W', 'P', 'I']
                           
        if (self.soe == 0):
            lis = ["A", "D", "F", "G", "V", "X"]
        elif (self.soe == 1):
            lis = ["T", "W", "U", "K", "Z", "X"]



            
        for i in range(len(lis)):
            for j in range(len(lis)):
                self.tableCipher.append(lis[i] + lis[j])
            
    def encode(self, S):
        semi = ""
        for i in range(len(S)):
            ch = S[i]
            semi += self.tableCipher[self.tablePlane.index(ch)]

        new = self.KCTob.encode(semi)
        return(new)
            

    def decode(self, S):
        semi = self.KCTob.decode(S)
        new = ""

        for i in range(int(len(semi)/2)):
            st = ""
            st += semi[2 * i] + semi[2 * i + 1]
            new += self.tablePlane[self.tableCipher.index(st)]

        return(new)
