# -*- coding: utf-8 -*-
"""
Created on Wed May 20 18:10:25 2020

@author: omeil
"""

from Affine import Affine
from Autokey import Autokey
from Hill import Hill
from KCT import KCT
from Permutation import Permutation as Per
from Vigenere import Vigenere as Vig

from IOC import IOC
from ProductSum import ProductSum

class Encrypt(object):
    def __init__(self, planeText, verbose = 0):
        self.planeText = planeText
        self.verbose = verbose

    def encodeAffine(self, m, n):
        """This definition encodes using an affine cipher with m being for a
        multiplicative cipher and n being for a shift cipher"""

        encode = Affine(m, n)
        cipherText = encode.encode(self.planeText)

        if (self.verbose == 1):
            print(cipherText)
            
        return(cipherText)


    def encodeAutokey(self, key):
        """
        """

        encode = Autokey(key)
        cipherText = encode.encode(self.planeText)

        if (self.verbose == 1):
            print(cipherText)

        return(cipherText)
        
        
    def encodeHill(self, k1, k2, k3, k4):
        encode = Hill(k1, k2, k3, k4)
        cipherText = encode.encode(self.planeText)
        
        if (self.verbose == 1):
            print(cipherText)
            
        return(cipherText)


    def encodeKCT(self, keyword):
        """ """

        encode = KCT(keyword)
        cipherText= encode.encode(self.planeText)
        
        if (self.verbose == 1):
            print(cipherText)
            
        return(cipherText)
    

    def encodePermutation(self, perm):
        """ugh"""

        encode = Per(perm)
        cipherText = encode.encode(self.planeText)
        
        if (self.verbose == 1):
            print(cipherText)
            
        return(cipherText)
        

    def encodeVigenere(self, key):
        """endodes using a key"""

        encode = Vig(key)
        cipherText = encode.encode(self.planeText)
        
        if (self.verbose == 1):
            print(cipherText)
            
        return(cipherText)




    def calcIOC(self):
        """this calulates the IOC from the planeText"""
        self._calcIOC(self.planeText)
        

    def _calcIOC(self, string):
        """this calulates the IOC from a passed string"""
        
        ob = IOC(string)
        ioc = ob.calcIOC

        if (self.verbose == 1):
            print(ioc)
            
        return(ioc)
    

    
class Decrypt(object):
    def __init__(self, cipherText, verbose = 0):
        self.cipherText = cipherText
        self.verbose = verbose

    def decodeAffine(self, m, n):
        """decoding an affine cipher with the known encryption key with m being 
        for a multiplicative cipher and n being for a shift cipher"""

        decode = Affine(m, n)
        planeText = decode.decode(self.cipherText)

        if (self.verbose == 1):
            print(planeText)
            
        return(planeText)


    def decodeAutokey(self, key):
        """
        """

        decode = Autokey(key)
        planeText = decode.decode(self.cipherText)

        if (self.verbose == 1):
            print(planeText)

        return(planeText)

        
    def decodeHill(self, k1, k2, k3, k4):
        decode = Hill(k1, k2, k3, k4)
        planeText = decode.decode(self.cipherText)
        
        if (self.verbose == 1):
            print(planeText)
            
        return(planeText)


    def decodeKCT(self, keyword):
        """ """

        decode = KCT(keyword)
        planeText = decode.decode(self.cipherText)
        
        if (self.verbose == 1):
            print(planeText)
            
        return(planeText)

    
    def decodePermutation(self, perm):
        """ugh"""

        decode = Per(perm)
        planeText = decode.decode(self.cipherText)
        
        if (self.verbose == 1):
            print(planeText)
            
        return(planeText)
    
    def decodeVigenere(self, key):
        """decode a viginere with known key"""

        decode = Vig(key)
        planeText = decode.decode(self.cipherText)
        
        if (self.verbose == 1):
            print(planeText)
            
        return(planeText)
        

    def calcIOC(self):
        """this calulates the IOC from the cipherText"""
        self._calcIOC(self.cipherText)
        

    def _calcIOC(self, string):
        """this calulates the IOC from a passed string"""
        
        ob = IOC(string)
        ioc = ob.calcIOC

        if (self.verbose == 1):
            print(ioc)
            
        return(ioc)






"""misc definitions that might be nice to just have"""

def calcIOC(string, verbose = 0):
    """this calulates the IOC from a passed string"""
    ob = IOC(string)
    ioc = ob.calcIOC

    if (verbose == 1):
        print(ioc)
            
    return(ioc)
