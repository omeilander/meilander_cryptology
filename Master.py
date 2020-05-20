# -*- coding: utf-8 -*-
"""
Created on Wed May 20 18:10:25 2020

@author: omeil
"""

from Affine import Affine
from Hill import Hill
from Vigenere import Vigenere

from IOC import IOC
from ProductSum import ProductSum

class Encrypt(object):
    def __init__(self, planeText, verbose = 0):
        self.planeText = planeText
        
    def encodeHill(self, k1, k2, k3, k4):
        encode = Hill(k1, k2, k3, k4)
        cipherText = encode.encode(self.planeText)
        
        if (verbose == 1):
            print(cipherText)
            
        return(cipherText)
        
        
class Decrypt(object):
    def __init__(self, cipherText):
        self.cipherText = cipherText