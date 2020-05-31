# -*- coding: utf-8 -*-
"""
Created on Wed May 20 21:21:21 2020

@author: omeil
"""
import numpy

class Permutation(object):
    """"""
    def __init__(self, perm):
        """"""
        
        self.perm = numpy.array(perm)-1
        self.block = len(self.perm)

    def encode(self, string, _forKCT = 0):
        """"""
        length = len(string)
        new = ""
        number = self.block - (length % self.block)
        counter = 0
        

        for i in range(number):
            string += 'X'

        while (counter < length / self.block):
            block = string[:self.block]
            string = string[self.block:]
            temp = []
            newButNumbers = []
            for i in range(self.block):
                temp.append(0)
                
            for i in range(self.block):
                temp[i] = block[self.perm[i]]

            for i in range(self.block):
                new += temp[i]

            counter += 1

        return(new)
        


    def decode(self, string):
        """"""
        length = len(string)
        new = ""
        number = self.block - (length % self.block)
        counter = 0
        
        if (number != self.block):
            for i in range(number):
                string += 'X'

        while (counter < length / self.block):
            block = string[:self.block]
            string = string[self.block:]
            temp = []
            for i in range(self.block):
                temp.append(0)
                
            for i in range(self.block):
                temp[self.perm[i]] = block[i]

            for i in range(self.block):
                new += temp[i]

            counter += 1
                

        return(new)
        
        
