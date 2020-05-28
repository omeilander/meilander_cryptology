# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 21:23:42 2020

@author: omeil
"""
from Master import Encrypt
from Master import Decrypt

S = "SECRETMESSAGETHISISVERYIMPORTANTDONOTTELLANYONEWHATTHISSAYS"
key = "EXPO"

enc = Encrypt(S, verbose = 1)

enc.encodeVigenere(key)

#============================================================================

S2 = "WBRFIQBSWPPUIQWWWFHJIONWQMDFXXCHHLCCXQTZPXCMSKTKLXIHLFHGEVH"

dec = Decrypt(S2, verbose = 1)

dec.decodeVigenere(key)
