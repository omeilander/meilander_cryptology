# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 17:27:44 2020

@author: omeil
"""

#TO RUN THROUGH ALL IT TAKES <4s for 20 letters (5l/s), <7s for 50 (7l/s), and 25s for 231 (9l/s)

from Hill import Hill

encode = "QWERTYUIOPASDFGHJKLZXCBVNMQWERTYUIOPASDFGHJKLZXCVB"
encode = "BCBMLDSXGQTGXPMWMZLBMESZBCPBMSPZQXRSACQHBCRSMXBPQOKBBMFSZKKQZCIMLTPQIXBCUQZXMKSQZQTBMIRCXGIMLZCGGDOXDCUMOGCGBCBMLGRCHXSZXBCRQTXQTGQICGXMDRCMZLSZGHSXCQTSXMRRGBCWMGDCMOXSTORWBMXMGXMPMPXXBQOQEQOXBSZXBCICMZXSICGBCBMLBMRXCLSZTPQZXQTIMPSOGWSXBMXPMUCQTJQESZBCPRSFSLUQOZXCZMZUCMZLGQICXBSZKWBSUBPCGCIDRCLMGISRCGBCGXQQLTQPGCFCPMRIQICZXGMGXBQOKBSZUMHMDRCQTGHCCUB"

k1 = 1
k2 = 1
k3 = 1
k4 = 1
for i in range(26):
    for j in range(26):
        for k in range(26):
            for l in range(26):
                
                hill = Hill(k1 % 26, k2 % 26, k3 % 26, k4 % 26)

                try:
                    decode = hill.decode(encode)
                except:
                    decode = "null"
                
                if (decode[0] == 'H' and decode[1] == "I" and decode[2] == 'A' and decode[3] == 'L'):
                    print(decode)
                    #print(k1 + k2 + k3 + k4)
                k4+=1
            k3+=1
        k2+=1
    k1+=1
