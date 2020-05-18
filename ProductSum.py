# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 23:41:40 2020

@author: omeil
"""

class ProductSum(object):
    
    def __init__(self, idk = 0):
        self.idk
        
    def productSum(self, A, F):
        psum = 0
        if (len(A) == len(F)):
            for i in range(len(A)):
                psum += A[i] * F[i]
            return psum
        
        else:
            return 0