# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 14:51:49 2020

@author: omeil
"""
import numpy as np
from Affine import Affine as A

S = "ZOZMJERSJPKRVTAUXAZOZMJVVQGZSJUWZDATLUWFTNSOPSDHZJQJSYPYWFQBMG"
m = 0
n = 0

aff = A(m ,n)
#aff.numLet(S)
aff.encode(S, True)
