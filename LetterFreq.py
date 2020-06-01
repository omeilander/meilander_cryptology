# -*- coding: utf-8 -*-
"""
Created on Sun May 31 19:28:45 2020

@author: omeil
"""
import numpy

class LetterFreq (object):
    
    def __init__(self, string):

        self.S = string

    def calcLF(self):
        lis = numpy.zeros(26)
        for i in range(len(self.S)):
            ch = self.S[i]
            num = ord(ch) - 65
            lis[num] += 1

        return(lis)
