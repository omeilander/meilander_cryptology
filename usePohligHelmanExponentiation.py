# -*- coding: utf-8 -*-
"""
Created on Tue June 9 14:06:47 2020

@author: omeil
"""

from Master import Encrypt
from Master import Decrypt

S = "SECRETMESSAGETHISISVERYIMPORTANTDONOTTELLANYONEWHATTHISSAYS"
e = 769

enc = Encrypt(S, verbose = 1)

enc.encodePohligHellman(e)

#============================================================================

S2 = "CDCHCEHDAAHJBCCHBHFDAGDJAAHJBADFAJFICHJCAJJBBHACBGBDCDIEAEEDBBIACHEIBJEHCFIEBBBHCDIBCCIBCBCHBDCAACCJCFIEBADFBHFDABCIADFI"

dec = Decrypt(S2, verbose = 1)

dec.decodePohligHellman(e)