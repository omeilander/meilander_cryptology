# -*- coding: utf-8 -*-
"""
Created on Fri June 6 21:09:16 2020

@author: omeil
"""
from Master import Encrypt
from Master import Decrypt

key = [1, 2, 0, 2, 9]
"""The key MUST be a list that is 5 integers long"""
S = "SECRETMESSAGETHISISVERYIMPORTANTDONOTTELLANYONEWHATTHISSAYS"

enc = Encrypt(S, verbose = 1)

enc.encodeGromark(key)

#============================================================================

S2 = "TGCTNWOGDEFKRQYRJSGVESWWMQNDHBNEDDOZEIUXHASAWJJDREUFYWXFDDL"

dec = Decrypt(S2, verbose = 1)

dec.decodeGromark(key)
