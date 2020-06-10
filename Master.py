# -*- coding: utf-8 -*-
"""
Created on Wed May 20 18:10:25 2020

@author: omeil
"""
import numpy

from Affine import Affine
from Autokey import Autokey
from GedeFu18 import GedeFu18
from Gromark import Gromark
from Hill import Hill
from KCT import KCT
from Permutation import Permutation as Per
from PohligHelmanExponentiation import PohHell
from Vigenere import Vigenere as Vig

from IOC import IOC
from KappaTest import Kappa
from LetterFreq import LetterFreq
from ProductSum import ProductSum

class Encrypt(object):
    def __init__(self, planeText, verbose = 0):
        self.planeText = planeText.upper().replace(" ", "")
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

        key = key.upper().replace(" ", "")
        encode = Autokey(key)
        cipherText = encode.encode(self.planeText)

        if (self.verbose == 1):
            print(cipherText)

        return(cipherText)


    def encodeGedeFu18(self, key):
        """
        """

        key = key.upper().replace(" ", "")
        encode = GedeFu18(key)
        cipherText = encode.encode(self.planeText)

        if (self.verbose == 1):
            print(cipherText)

        return(cipherText)


    def encodeGromark(self, key):
        """
        """

        encode = Gromark(key)
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

        keyword = keyword.upper().replace(" ", "")
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
    

    def encodePohligHellman(self, e, mod = 2819):
        """ugh"""

        encode = PohHell(e, modulo = mod)
        cipherText = encode.encode(self.planeText)
        
        if (self.verbose == 1):
            print(cipherText)
            
        return(cipherText)
        

    def encodeVigenere(self, key):
        """endodes using a key"""

        key = key.upper().replace(" ", "")
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
        self.cipherText = cipherText.upper().replace(" ", "")
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

        key = key.upper().replace(" ", "")
        decode = Autokey(key)
        planeText = decode.decode(self.cipherText)

        if (self.verbose == 1):
            print(planeText)

        return(planeText)


    def decodeGedeFu18(self, key):
        """
        """

        key = key.upper().replace(" ", "")
        decode = GedeFu18(key)
        planeText = decode.decode(self.cipherText)

        if (self.verbose == 1):
            print(planeText)

        return(planeText)


    def decodeGromark(self, key):
        """
        """

        decode = Gromark(key)
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

        keyword = keyword.upper().replace(" ", "")
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

    
    def decodePohligHellman(self, e, mod = 2819):
        """ugh"""

        decode = PohHell(e, modulo = mod)
        planeText = decode.decode(self.cipherText)
        
        if (self.verbose == 1):
            print(planeText)
            
        return(planeText)

    
    def decodeVigenere(self, key):
        """decode a viginere with known key"""

        key = key.upper().replace(" ", "")
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


#===========================================================


class Tests(object):
    def __init__(self, String, verbose = 1):
        self.S = String.upper().replace(" ", "")
        self.verbose = verbose


    def calcIOC(self):
        """this calulates the IOC from the passed string"""
        ioc = self._calcIOC(self.S)
        return ioc


    def calcKappa(self, numTests = 25):
        """ """

        test = Kappa(self.S)
        num = test.calcKappa(num_tested = numTests)

        if (self.verbose == 1):
            prt_num = numpy.arange(0, numTests + 1, 1)

            print("Kappa Test:")
            for i in range(numTests + 1):
                prcnt = num [i] / len(self.S)
                print("{:2.0f}: {:3.0f}      {:.3f}".format(prt_num[i], num[i], prcnt))
            
        return(num)


    def calcLetterFreq(self):
        """ """

        test = LetterFreq(self.S)
        lis = test.calcLF()

        if (self.verbose == 1):
            letters = numpy.arange(0, 26, 1)
            print("Letter Frequency Table")
            for i in range(len(lis)):
                print("{:2.0f}({}):  {:3.0f}".format(letters[i], chr(letters[i] + 65), lis[i]))

        return(lis)
    

    def _calcIOC(self, string):
        """this calulates the IOC from a passed string"""
        
        ob = IOC(string)
        ioc = ob.calcIOC()

        if (self.verbose == 1):
            print(ioc)
            
        return(ioc)
