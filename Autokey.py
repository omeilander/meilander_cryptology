# -*- coding: utf-8 -*-
"""
Created on Fri May 29 21:09:16 2020

@author: omeil
"""

class Autokey(object):
    def __init__(self, key):
        self.key = []
        for i in range(len(key)):
            self.key.append(ord(key[i]) - 65)

    def encode(self, S):
        new = ""
        for i in range(len(S)):
            letter = (ord(S[i]) - 65)
            self.key.append(letter)
            letter = (letter + self.key[i]) % 26
            ch = chr((letter + 65))
            new += ch

        return(new)

    def decode(self, S):
        new = ""
        for i in range(len(S)):
            letter = (ord(S[i]) - 65)
            letter = (letter - self.key[i]) % 26
            self.key.append(letter)
            ch = chr((letter + 65))
            new += ch

        return(new)
