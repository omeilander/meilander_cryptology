# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 00:17:30 2020

@author: omeil
"""

from Affine import Affine as A

S = "JLOQFLABDCKEJPVKFPBPPOQEPXKQTLEVOXBQPK"
m = 0
n = 0

aff = A(m ,n)
#aff.numLet(S)
aff.encodefs(S, True)