# -*- coding: utf-8 -*-
"""
Created on Sun May 31 19:28:45 2020

@author: omeil
"""

class Kappa (object):

    def __init__(self, String):

        self.S = String

    def calcKappa(self, num_tested = 25):

        S2 = self.S + self. S
        num = []

        for i in range(num_tested + 1):
            temp = 0
            for j in range(len(self.S)):
                if (self.S[j] == S2[j+i]):
                    temp += 1

            num.append(temp)

        return(num)
