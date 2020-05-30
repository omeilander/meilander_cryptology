# -*- coding: utf-8 -*-
"""
Created on Fri May 29 21:09:16 2020

@author: omeil
"""

from Master import Encrypt
from Master import Decrypt

from Autokey import Autokey

S = "SECRETMESSAGETHISISVERYIMPORTANTDONOTTELLANYONEWHATTHISSAYS"
key = "EXPO"

enc = Encrypt(S, verbose = 1)

enc.encodeAutokey(key)

#============================================================================

S2 = "WBRFWXOVWLMKWLHOWBZDWZQDQGMZFPBKWOAHWHRZETRJZNRUVNXPOILLHGK"

dec = Decrypt(S2, verbose = 1)

dec.decodeAutokey(key)

