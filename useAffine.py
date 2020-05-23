# -*- coding: utf-8 -*-
"""
This program is an example of how to use the Master program 
to encrypt and decrypt using an Affine Cipher.
"""
from Master import Encrypt
from Master import Decrypt

S = "SECRETMESSAGETHISISVERYIMPORTANTDONOTTELLANYONEWHATTHISSAYS"
m = 3
n = 7

enc = Encrypt(S, verbose = 1)

enc.encodeAffine(m, n)

#============================================================================

S2 = "JTNGTMRTJJHZTMCFJFJSTGBFRAXGMHUMQXUXMMTOOHUBXUTVCHMMCFJJHBJ"

dec = Decrypt(S2, verbose = 1)

dec.decodeAffine(m, n)
