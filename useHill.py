# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 17:27:44 2020

@author: omeil
"""

from Master import Encrypt
from Master import Decrypt

S = "SECRETMESSAGETHISISVERYIMPORTANTDONOTTELLANYONEWHATTHISSAYS"

k1 = 5
k2 = 9
k3 = 3
k4 = 6

enc = Encrypt(S, verbose = 1)

enc.encodeHill(k1, k2, k3, k4)

#============================================================================

S2 = "WAHEJWSISGCKJWDRGYTYRKKQNWPORFCXLPJTGPPADHVBFQKOJVGPDRSGIOLK"

dec = Decrypt(S2, verbose = 1)

dec.decodeHill(k1, k2, k3, k4)

