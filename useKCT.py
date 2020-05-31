# -*- coding: utf-8 -*-
"""
Created on Wed May 30 21:21:21 2020

@author: omeil
"""

from Master import Encrypt
from Master import Decrypt


S = "SECRETMESSAGETHISISVERYIMPORTANTDONOTTELLANYONEWHATTHISSAYS"
keyword = "MENTAL"

enc = Encrypt(S, verbose = 1)

enc.encodeKCT(keyword)

#============================================================================

S2 = "EASYTNLEHSEETVPTTYASTGIIAOAWIXSMESMNTNHSCSHEODEOTARSIRROLNTY"

dec = Decrypt(S2, verbose = 1)

dec.decodeKCT(keyword)


