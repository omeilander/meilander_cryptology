# -*- coding: utf-8 -*-
"""
Created on Wed May 30 21:21:21 2020

@author: omeil
"""
import numpy
from Permutation import Permutation as Perm

class KCT(object):

    def __init__(self, key):

        self.keynum = []
        self.key = key
        self.length = len(key)
        self.perm = numpy.arange(1, self.length + 1, 1)

        for i in range(len(key)):
            self.keynum.append(ord(key[i]) - 65)

        self._getperm()

        
    def _getperm(self):

        i = 0
        while (i < len(self.key)):
            j = i + 1
            while (j < len(self.key)):
                if (self.keynum[i] > self.keynum[j]):
                    temp = self.keynum[j]
                    temp2 = self.perm[j]
                    
                    self.keynum[j] = self.keynum[i]
                    self.keynum[i] = temp

                    self.perm[j] = self.perm[i]
                    self.perm[i] = temp2
                j += 1
            i += 1
        return


    def encode(self, S):

        enc = Perm(self.perm)
        st = enc.encode(S)

        new = ""

        num_rows = len(st) / len(self.perm)

        for i in range(len(self.perm)):
            for j in range(int(num_rows)):

                new += st[len(self.perm) * j + i]

        return new


    def decode(self, S):

        dec = Perm(self.perm)
        st = ""
        num_rows = int(len(S) / len(self.perm))
        
        for i in range((num_rows)):
            for j in range(len(self.perm)):

                st += S[num_rows * j + i]

        new = dec.decode(st)

        return(new)

                
