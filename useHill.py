# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 17:27:44 2020

@author: omeil
"""

from Hill import Hill

s = "BLUEFROGS"
#encode = "SPDSXDWWZENWSFIOMVEL"

k1 = 2
k2 = 5
k3 = 7
k4 = 1

hill = Hill(k1, k2, k3, k4)

encode = hill.encode(s)
print(encode)

decode = hill.decode(encode)
print(decode)
