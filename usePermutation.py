# -*- coding: utf-8 -*-
"""
Created on Wed May 20 21:36:03 2020

@author: omeil
"""
from Master import Encrypt
from Master import Decrypt

S = "SECRETMESSAGETHISISVERYIMPORTANTDONOTTELLANYONEWHATTHISSAYS"
perm = [2, 4, 1, 3]

enc = Encrypt(S, verbose = 1)

enc.encodePermutation(perm)

#============================================================================

S2 = "ERSCTEEMSGSATIEHIVSSRIEYPRMOATTNOODNTLTEAYLNNWOEATHTISHSYXAS"

dec = Decrypt(S2, verbose = 1)

dec.decodePermutation(perm)
