# -*- coding: utf-8 -*-
"""
Created on Tue June 9 14:06:47 2020

@author: omeil
"""

class PohHell(object):
    def __init__(self, e, modulo = 2819):
        self.e = e
        self.mod = modulo

    def encode(self, S):
        new = ""
        if (len(S) % 2 == 1):
            S += "X"

        for i in range(int(len(S)/2)):
            one = str(ord(S[2 * i]) - 65)

            if (ord(S[2 * i + 1]) - 65 < 10):
                two = "0" + str(ord(S[2 * i + 1]) - 65)

            else:
                two = str(ord(S[2 * i + 1]) - 65)

            tot = str(int(one + two) ** self.e % self.mod)
            while len(tot) < 4:
                tot = "0" + tot
            #print(tot)

            new += (chr(int(tot[0]) + 65) + chr(int(tot[1]) + 65) + chr(int(tot[2]) + 65) + chr(int(tot[3]) + 65))
        return(new)

    def decode(self, S):
        new = ""
        d = self.modInverse(self.e, self.mod - 1)
        st = ""
        for i in range(len(S)):
            st += str(ord(S[i]) - 65)

        for i in range(int(len(S) / 4)):
            num = int(st[(i * 4): ((i + 1) * 4)])
            tot = str(num ** d % self.mod)

            if len(tot) == 1:
                new += chr(65)
                new += chr(int(tot) + 65)

            elif len(tot) == 2:
                new += chr(65)
                new += chr(int(tot) + 65)

            elif len(tot) == 3:
                new += chr(int(tot[0]) + 65)
                new += chr(int(tot[1:]) + 65)

            else:
                new += chr(int(tot[0:2]) + 65)
                new += chr(int(tot[2:]) + 65)
        return(new)




#==================================================================
    def modInverse(self, a, m) : 
        m0 = m 
        y = 0
        x = 1
      
        if (m == 1) : 
            return 0
      
        while (a > 1) : 
      
            q = a // m 
      
            t = m 
      
            m = a % m 
            a = t 
            t = y 
      
            y = x - q * y 
            x = t 
      
      
        if (x < 0) : 
            x = x + m0 
      
        return(x) 
