# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 15:46:45 2020

@author: omeil
"""
import Vigenere as VV
from Vigenere import Vigenere as Vin
import numpy as np

pr = True

fake = Vin("FAKE")
cipher = "OCNYBIFHBRUPBNYAZGBBNBYESSYXYYNSQVMFDCHDNCSWHTEGNPMNLRSWXRYPPAFNGBUCFNGBISLRTRPILFXYXOMUXBTIHFXRHONRLQIOFYLRBBXNFGHVNLPMNOHJBRIONBKAIKBBLCGZUZXGTHBRBKQFCFHLFRFVZFUBCAZYORBRKLBAYZHRISLBYCYWFRLDSCGUXPCSUPHLIOHQZJPKMJHPMRQVWCXSFPHKFVYEFGMRYLXQDCGZTLEHBRTGSPLVWEFRBNKZPFNUTRUKCAVGUWYFYPBAYXXCQOHPBCOHFNGBTMIHKQUCLVXBQCGCVPJSMFACXWNULGMSHGEGQGAVOCNSSBNPUWLRWWPILCHMSMIHKFVRXYXBNOMFXQZSUEGGOUNBUPFONUXDSSYGACXFYGVFFRLRYSTSISRMVFNRXKJBAFAMSSMRGBUVYFXRISBBFCMSMFMCNDYFMRPGNGHKFWFVYRNMFNFNCSMVWCUVYTHJESHQHMS"
ln = VV.findL(cipher)

#keyholder = np.zeros(l)


for i in range(26):
    for j in range(26):
        for k in range(26):
            for l in range(26):
                for m in range(26):
                    for n in range(26):
                        keyholder = np.array((i, j, k, l, m, n))
                        key = ""
                        for i in range(len(keyholder)):
                            ch = chr((keyholder[i] % 26) + 65)
                            key += ch
                        vin = Vin(key)
                        decode = vin.decode(cipher)
                        if (pr == True):
                            print(decode)
