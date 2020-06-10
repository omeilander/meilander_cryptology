# -*- coding: utf-8 -*-
"""
Created on Fri June 6 21:09:16 2020

@author: omeil
"""


class Gromark(object):
    def __init__(self, key):
        """the key must be a list of five integers between 0-25"""
        self.key = key

    def encode(self, S):
        new = ""
        for i in range(len(S)):
            letter = ord(S[i]) - 65
            self.key.append((self.key[i] + self.key[i + 1]) % 26)

            new += chr(((letter + self.key[i]) % 26) + 65)

        return(new)


    def decode(self, S):
        new = ""
        for i in range(len(S)):
            letter = ord(S[i]) - 65
            self.key.append((self.key[i] + self.key[i + 1]) % 26)

            new += chr(((letter - self.key[i]) % 26) + 65)

        return(new)
