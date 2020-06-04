# -*- coding: utf-8 -*-
"""
Created on Wed June 3 19:28:45 2020

@author: omeil
"""
from Master import Encrypt
from Master import Decrypt

key = "GERMANY"
S = "SECRETMESSAGETHISISVERYIMPORTANTDONOTTELLANYONEWHATTHISSAYS"

enc = Encrypt(S, verbose = 1)

enc.encodeGedeFu18(key)

#============================================================================

S2 = "AAFGFVXXVXGFVGGDFDFGVAFFXADXFAFDXDFFFDXXDDGAVGVAXAXGGDFXVDVDVAFDXAFDXGDGDFXDAVAXXXAFDFGFDXDDVXVGFDGGXDDDXAXGGFGAFDVAXDX"

dec = Decrypt(S2, verbose = 1)

dec.decodeGedeFu18(key)
