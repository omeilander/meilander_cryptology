# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 19:28:45 2020

@author: omeil
"""

from Master import Encrypt
from Master import Decrypt
from Master import Tests
from tkinter import *
from tkinter import messagebox
import numpy

root = Tk()
root.title('Bosley Encryption')
root.iconbitmap("bosley.ico")

init = 0

def Close():
    print("oops... I havent gotten here yet...")


#=======================================================================================================

"""
Comment
"""

def IOC(S):
    tst = Tests(S, verbose = 0)

    ioc = tst.calcIOC()

    out = Toplevel()
    out.title('IOC Result')
    txt = "The Index of Coincidence is:"
    Label(out, text = txt).grid(row = 0, column = 0, columnspan = 5, padx = 30 , pady = 10)
    e = Entry(out, width = 25)
    e.grid(row = 1, column = 0, columnspan = 5, padx = 10 , pady = 10)
    e.insert(0, ioc)

    close = Button(out, text = "Close", padx = 20 , pady = 10, command = Close).grid(row = 2, column = 2, padx = 10 , pady = 10)

def Kappa(S):
    tst = Tests(S, verbose = 0)

    def subm(nt):
        num = tst.calcKappa(numTests = int(nt))
        prt_num = numpy.arange(0, int(nt) + 1, 1)

        Label(out, text = "Kappa Test Result:").grid(row = 3, column = 0, columnspan = 5, padx = 30 , pady = 10)
        for i in range(int(nt) + 1):
            prcnt = num [i] / len(S)
            Label(out, text = "{:2.0f}: {:3.0f}      {:.3f}".format(prt_num[i], num[i], prcnt)).grid(row = i + 4, column = 0, columnspan = 5, padx = 10 )

        close = Button(out, text = "Close", padx = 20 , pady = 10, command = Close).grid(row =int(nt) + 5 , column = 2, padx = 10 , pady = 10)


    out = Toplevel()
    out.title('Kappa Result')
    txt = "Please enter the number of tests you want."
    Label(out, text = txt).grid(row = 0, column = 0, columnspan = 5, padx = 30 , pady = 10)
    e = Entry(out, width = 10)
    e.grid(row = 1, column = 0, columnspan = 5, padx = 10 , pady = 10)
    e.insert(0, 25)

    sub = Button(out, text = "Submit", padx = 20 , pady = 10, command = lambda: subm(e.get())).grid(row = 2, column = 2, padx = 10 , pady = 10)
    

def LF(S):
    tst = Tests(S, verbose = 0)
    letters = numpy.arange(0, 26, 1)

    lis = tst.calcLetterFreq()

    out = Toplevel()
    out.title('Letter Frequency Result')
    txt = "The Letter Frequency is as follows:"
    Label(out, text = txt).grid(row = 0, column = 0, columnspan = 5, padx = 30 , pady = 10)

    for i in range(26):
        Label(out, text = "{:2.0f}({}):  {:3.0f}".format(letters[i], chr(letters[i] + 65), lis[i])).grid(row = i + 1, column = 0, columnspan = 5, padx = 10 )

    close = Button(out, text = "Close", padx = 20 , pady = 10, command = Close).grid(row = 27, column = 2, padx = 10 , pady = 10) 
    

    
#=======================================================================================================

"""
Comment
"""

def AffineEncode(S, m, n):
    if (int(m) == 13):
        response  = messagebox.showwarning("Uh Oh!", "Sigh... I'm sorry m cannot be 13... I know I just said odd but it was too long to put in the box so here's your warning.")
        return
    
    m = int(m)
    n = int(n)
    enc = Encrypt(S)
    
    out = Toplevel()
    out.title('Ciphertext')
    txt = "The ciphertext is as follows:"
    Label(out, text = txt).grid(row = 0, column = 0, columnspan = 5, padx = 10 , pady = 10)
    e = Entry(out, width = 100)
    e.grid(row = 1, column = 0, columnspan = 5, padx = 10 , pady = 10)
    e.insert(0, enc.encodeAffine(m, n))

    close = Button(out, text = "Close", padx = 20 , pady = 10, command = Close).grid(row = 2, column = 2, padx = 10 , pady = 10) 
    

def AutoEncode(S, key):
    enc = Encrypt(S)

    out = Toplevel()
    out.title('Ciphertext')
    txt = "The ciphertext is as follows:"
    Label(out, text = txt).grid(row = 0, column = 0, columnspan = 5, padx = 10 , pady = 10)
    e = Entry(out, width = 100)
    e.grid(row = 1, column = 0, columnspan = 5, padx = 10 , pady = 10)
    e.insert(0, enc.encodeAutokey(key))

    close = Button(out, text = "Close", padx = 20 , pady = 10, command = Close).grid(row = 2, column = 2, padx = 10 , pady = 10)


def HillEncode(S, k1, k2, k3, k4):
    if (int(k1) * int(k4) == int(k2) * int(k3)):
        response  = messagebox.showwarning("Uh Oh!", "k1 * k4 cannot equal k2 * k3")
        return
    
    k1 = int(k1)
    k2 = int(k2)
    k3 = int(k3)
    k4 = int(k4)
    enc = Encrypt(S)
    
    out = Toplevel()
    out.title('Ciphertext')
    txt = "The ciphertext is as follows:"
    Label(out, text = txt).grid(row = 0, column = 0, columnspan = 5, padx = 10 , pady = 10)
    e = Entry(out, width = 100)
    e.grid(row = 1, column = 0, columnspan = 5, padx = 10 , pady = 10)
    e.insert(0, enc.encodeHill(k1, k2, k3, k4))

    close = Button(out, text = "Close", padx = 20 , pady = 10, command = Close).grid(row = 2, column = 2, padx = 10 , pady = 10)
    

def KCTEncode(S, key):
    enc = Encrypt(S)

    out = Toplevel()
    out.title('Ciphertext')
    txt = "The ciphertext is as follows:"
    Label(out, text = txt).grid(row = 0, column = 0, columnspan = 5, padx = 10 , pady = 10)
    e = Entry(out, width = 100)
    e.grid(row = 1, column = 0, columnspan = 5, padx = 10 , pady = 10)
    e.insert(0, enc.encodeKCT(key))

    close = Button(out, text = "Close", padx = 20 , pady = 10, command = Close).grid(row = 2, column = 2, padx = 10 , pady = 10)
    

def PermEncode(S, func):
    perm = []
    
    for i in range(len(func)):
        perm.append(int(func[i].get()))

    out = Toplevel()
    enc = Encrypt(S)
    out.title('Ciphertext')
    txt = "The ciphertext is as follows:"
    Label(out, text = txt).grid(row = 0, column = 0, columnspan = 5, padx = 10 , pady = 10)
    e = Entry(out, width = 100)
    e.grid(row = 1, column = 0, columnspan = 5, padx = 10 , pady = 10)
    e.insert(0, enc.encodePermutation(perm))

    close = Button(out, text = "Close", padx = 20 , pady = 10, command = Close).grid(row = 2, column = 2, padx = 10 , pady = 10)
    

def VigEncode(S, key):
#    check
    enc = Encrypt(S)

    out = Toplevel()
    out.title('Ciphertext')
    txt = "The ciphertext is as follows:"
    Label(out, text = txt).grid(row = 0, column = 0, columnspan = 5, padx = 10 , pady = 10)
    e = Entry(out, width = 100)
    e.grid(row = 1, column = 0, columnspan = 5, padx = 10 , pady = 10)
    e.insert(0, enc.encodeVigenere(key))

    close = Button(out, text = "Close", padx = 20 , pady = 10, command = Close).grid(row = 2, column = 2, padx = 10 , pady = 10)
    

#======================================================================================================

"""
Comment
"""

def AffineDecode(S, m, n):
    if (int(m) == 13):
        response  = messagebox.showwarning("Uh Oh!", "Sigh... I'm sorry m cannot be 13... I know I just said odd but it was too long to put in the box so here's your warning.")
        return
    
    m = int(m)
    n = int(n)
    dec = Decrypt(S)
    
    out = Toplevel()
    out.title('Ciphertext')
    txt = "The ciphertext is as follows:"
    Label(out, text = txt).grid(row = 0, column = 0, columnspan = 5, padx = 10 , pady = 10)
    e = Entry(out, width = 100)
    e.grid(row = 1, column = 0, columnspan = 5, padx = 10 , pady = 10)
    e.insert(0, dec.decodeAffine(m, n))

    close = Button(out, text = "Close", padx = 20 , pady = 10, command = Close).grid(row = 2, column = 2, padx = 10 , pady = 10)
    

def AutoDecode(S, key):
    dec = Decrypt(S)

    out = Toplevel()
    out.title('Ciphertext')
    txt = "The plaintext is as follows:"
    Label(out, text = txt).grid(row = 0, column = 0, columnspan = 5, padx = 10 , pady = 10)
    e = Entry(out, width = 100)
    e.grid(row = 1, column = 0, columnspan = 5, padx = 10 , pady = 10)
    e.insert(0, dec.decodeAutokey(key))

    close = Button(out, text = "Close", padx = 20 , pady = 10, command = Close).grid(row = 2, column = 2, padx = 10 , pady = 10)


def HillDecode(S, k1, k2, k3, k4):
    if (int(k1) * int(k4) == int(k2) * int(k3)):
        response  = messagebox.showwarning("Uh Oh!", "k1 * k4 cannot equal k2 * k3")
        return
    
    k1 = int(k1)
    k2 = int(k2)
    k3 = int(k3)
    k4 = int(k4)
    dec = Decrypt(S)

    
    out = Toplevel()
    out.title('Ciphertext')
    txt = "The ciphertext is as follows:"
    Label(out, text = txt).grid(row = 0, column = 0, columnspan = 5, padx = 10 , pady = 10)
    e = Entry(out, width = 100)
    e.grid(row = 1, column = 0, columnspan = 5, padx = 10 , pady = 10)
    e.insert(0, dec.decodeHill(k1, k2, k3, k4))

    close = Button(out, text = "Close", padx = 20 , pady = 10, command = Close).grid(row = 2, column = 2, padx = 10 , pady = 10)
    

def KCTDecode(S, key):
    dec = Decrypt(S)

    out = Toplevel()
    out.title('Ciphertext')
    txt = "The plaintext is as follows:"
    Label(out, text = txt).grid(row = 0, column = 0, columnspan = 5, padx = 10 , pady = 10)
    e = Entry(out, width = 100)
    e.grid(row = 1, column = 0, columnspan = 5, padx = 10 , pady = 10)
    e.insert(0, dec.decodeKCT(key))

    close = Button(out, text = "Close", padx = 20 , pady = 10, command = Close).grid(row = 2, column = 2, padx = 10 , pady = 10)


def PermDecode(S, func):
    perm = []
    
    for i in range(len(func)):
        perm.append(int(func[i].get()))

    out = Toplevel()
    dec = Decrypt(S)
    out.title('Planetext')
    txt = "The planetext is as follows:"
    Label(out, text = txt).grid(row = 0, column = 0, columnspan = 5, padx = 10 , pady = 10)
    e = Entry(out, width = 100)
    e.grid(row = 1, column = 0, columnspan = 5, padx = 10 , pady = 10)
    e.insert(0, dec.decodePermutation(perm))

    close = Button(out, text = "Close", padx = 20 , pady = 10, command = Close).grid(row = 2, column = 2, padx = 10 , pady = 10)

def VigDecode(S, key):
#    check
    dec = Decrypt(S)

    out = Toplevel()
    out.title('Ciphertext')
    txt = "The plaintext is as follows:"
    Label(out, text = txt).grid(row = 0, column = 0, columnspan = 5, padx = 10 , pady = 10)
    e = Entry(out, width = 100)
    e.grid(row = 1, column = 0, columnspan = 5, padx = 10 , pady = 10)
    e.insert(0, dec.decodeVigenere(key))

    close = Button(out, text = "Close", padx = 20 , pady = 10, command = Close).grid(row = 2, column = 2, padx = 10 , pady = 10)
    

#=====================================================================================================

"""
Comment
"""
    
def aff_en(planetext):
    aff_en = Toplevel()
    aff_en.title('Affine Encryption')
    
    txt = "Select a value for m and n where m and n are for the multiplicative and shift ciphers respectivly"
    l = Label(aff_en, text = txt).grid(row = 0, column = 0, columnspan = 5, padx = 10 , pady = 10)
    
    num_m = IntVar()
    num_m.set(1)
    n_m = numpy.array((1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25))
    m = OptionMenu(aff_en, num_m, *n_m)
    m.grid(row = 1, column = 1)
    Label(aff_en, text = "m").grid(row = 2, column = 1)

    num_n = IntVar()
    num_n.set(1)
    n_n = numpy.arange(1, 27, 1) 
    n = OptionMenu(aff_en, num_n, *n_n)
    n.grid(row = 1, column = 3)
    Label(aff_en, text = "n").grid(row = 2, column = 3)

    sub = Button(aff_en, text = "Submit", padx = 20 , pady = 10, command = lambda: AffineEncode(planetext, num_m.get(), num_n.get())).grid(row = 3, column = 2) 

def auto_en(planetext):
    auto_en = Toplevel()
    auto_en.title("Autokey Encryption")

    txt = "                    Enter a Keyword to encrypt with                    "
    l = Label(auto_en, text = txt).grid(row = 0, column = 0, columnspan = 5, padx = 10 , pady = 10)

    key = Entry(auto_en, width = 10)
    key.grid(row = 1, column = 2)
    keyl = Label(auto_en, text = "Keyword").grid(row = 2, column = 2)

    sub = Button(auto_en, text = "Submit", padx = 20 , pady = 10, command = lambda: AutoEncode(planetext, key.get())).grid(row = 3, column = 2)
    
def hill_en(planetext):    
    hill_en = Toplevel()
    hill_en.title('Hill Encryption')

    txt = "Enter a k1, k2, k3, and k4 to encrypt using a Hill cipher"
    l = Label(hill_en, text = txt).grid(row = 0, column = 0, columnspan = 5, padx = 10 , pady = 10)
    
    num_k1 = IntVar()
    num_k1.set(1)
    n_k1 = numpy.arange(1, 27, 1)
    k1 = OptionMenu(hill_en, num_k1, *n_k1)
    k1.grid(row = 1, column = 1)
    Label(hill_en, text = "k1").grid(row = 2, column = 1)
    
    num_k2 = IntVar()
    num_k2.set(1)
    k2 = OptionMenu(hill_en, num_k2, *n_k1)
    k2.grid(row = 1, column = 3)
    Label(hill_en, text = "k2").grid(row = 2, column = 3)
    
    num_k3 = IntVar()
    num_k3.set(1)
    k3 = OptionMenu(hill_en, num_k3, *n_k1)
    k3.grid(row = 3, column = 1)
    Label(hill_en, text = "k3").grid(row = 4, column = 1)
    
    num_k4 = IntVar()
    num_k4.set(1)
    k4 = OptionMenu(hill_en, num_k4, *n_k1)
    k4.grid(row = 3, column = 3)
    Label(hill_en, text = "k4").grid(row = 4, column = 3)

    sub = Button(hill_en, text = "Submit", padx = 20 , pady = 10, command = lambda: HillEncode(planetext, num_k1.get(), num_k2.get(), num_k3.get(), num_k4.get())).grid(row = 5, column = 2) 

def KCT_en(planetext):
    KCT_en = Toplevel()
    KCT_en.title("Keyed Columnar Transposition Encryption")

    txt = "                    Enter a Keyword to encrypt with                    "
    l = Label(KCT_en, text = txt).grid(row = 0, column = 0, columnspan = 5, padx = 10 , pady = 10)

    key = Entry(KCT_en, width = 10)
    key.grid(row = 1, column = 2)
    keyl = Label(KCT_en, text = "Keyword").grid(row = 2, column = 2)

    sub = Button(KCT_en, text = "Submit", padx = 20 , pady = 10, command = lambda: KCTEncode(planetext, key.get())).grid(row = 3, column = 2) 

def perm_en(planetext):
    perm_en = Toplevel()
    perm_en.title("Permutation Encryption")

    def block_perm_en(planetext, bs):
        txt = "                    Enter Block Size                    "
        l = Label(perm_en, text = txt).grid(row = 4, column = 0, columnspan = int(bs), padx = 10 , pady = 10)
        bs_int = int(bs)
        options = []
        number = []

        for i in range(bs_int):
            options.append(i+1)
            number.append(IntVar())

        for i in range(bs_int):
            num = str(i+1)
            drop = OptionMenu(perm_en, number[i], *options)
            drop.grid(row = 5, column = i, padx = 10 , pady = 10)
            bsl = Label(perm_en, text = num).grid(row = 6, column = i)
        l2 = Label(perm_en, text = "(You should not repeat numbers unless you want to loose information)").grid(row = 7, column = 0, columnspan = int(bs), padx = 10 , pady = 10)
        b = Button(perm_en, text = "Submit", command = lambda: PermEncode(planetext, number))
        b.grid(row = 8, column = 0 ,columnspan = bs_int, padx = 10 , pady = 10)
    
    txt = "                    Enter Block Size                    "
    l = Label(perm_en, text = txt).grid(row = 0, column = 0, columnspan = 5, padx = 10 , pady = 10)

    bs = Entry(perm_en, width = 10)
    bs.grid(row = 1, column = 2)
    bsl = Label(perm_en, text = "Block Size").grid(row = 2, column = 2)

    sub = Button(perm_en, text = "Next", padx = 20 , pady = 10, command = lambda: block_perm_en(planetext, bs.get())).grid(row = 3, column = 2) 

def vig_en(planetext):
    vig_en = Toplevel()
    vig_en.title("Vienére Encryption")

    txt = "                    Enter a Keyword to encrypt with                    "
    l = Label(vig_en, text = txt).grid(row = 0, column = 0, columnspan = 5, padx = 10 , pady = 10)

    key = Entry(vig_en, width = 10)
    key.grid(row = 1, column = 2)
    keyl = Label(vig_en, text = "Keyword").grid(row = 2, column = 2)

    sub = Button(vig_en, text = "Submit", padx = 20 , pady = 10, command = lambda: VigEncode(planetext, key.get())).grid(row = 3, column = 2) 

    
#======================================================================================================

"""
Comment
"""
    
def aff_de(ciphertext):
    aff_de = Toplevel()
    aff_de.title('Affine Decryption')
    
    txt = "Select the value for m and n where m and n are for the multiplicative and shift ciphers respectivly that were used"
    l = Label(aff_de, text = txt).grid(row = 0, column = 0, columnspan = 5, padx = 10 , pady = 10)
    
    num_m = IntVar()
    num_m.set(1)
    n_m = numpy.array((1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25))
    m = OptionMenu(aff_de, num_m, *n_m)
    m.grid(row = 1, column = 1)

    num_n = IntVar()
    num_n.set(1)
    n_n = numpy.arange(1, 27, 1) 
    n = OptionMenu(aff_de, num_n, *n_n)
    n.grid(row = 1, column = 3)

    sub = Button(aff_de, text = "Submit", padx = 20 , pady = 10, command = lambda: AffineDecode(ciphertext, num_m.get(), num_n.get())).grid(row = 3, column = 2) 

def auto_de(ciphertext):
    auto_de = Toplevel()
    auto_de.title("Autokey Decryption")

    txt = "                    Enter a Keyword to decrypt with                    "
    l = Label(auto_de, text = txt).grid(row = 0, column = 0, columnspan = 5, padx = 10 , pady = 10)

    key = Entry(auto_de, width = 10)
    key.grid(row = 1, column = 2)
    keyl = Label(auto_de, text = "Keyword").grid(row = 2, column = 2)

    sub = Button(auto_de, text = "Submit", padx = 20 , pady = 10, command = lambda: AutoDecode(ciphertext, key.get())).grid(row = 3, column = 2)
    
def hill_de(ciphertext):
    hill_de = Toplevel()
    hill_de.title('Hill Decryption')

    txt = "Enter a k1, k2, k3, and k4 to encrypt using a Hill cipher"
    l = Label(hill_de, text = txt).grid(row = 0, column = 0, columnspan = 5, padx = 10 , pady = 10)

    k1 = Entry(hill_de, width = 10)
    k1.grid(row = 1, column = 1)
    k11 = Label(hill_de, text = "k1").grid(row = 2, column =  1)
    k1.insert(0, "1-26")
    
    k2 = Entry(hill_de, width = 10)
    k2.grid(row = 1, column = 3)
    k21 = Label(hill_de, text = "k2").grid(row = 2, column =  3)
    k2.insert(0, "1-26")
    
    k3 = Entry(hill_de, width = 10)
    k3.grid(row = 3, column = 1)
    k31 = Label(hill_de, text = "k3").grid(row = 4, column =  1)
    k3.insert(0, "1-26")
    
    k4 = Entry(hill_de, width = 10)
    k4.grid(row = 3, column = 3)
    k41 = Label(hill_de, text = "k4").grid(row = 4, column =  3)
    k4.insert(0, "1-26")

    sub = Button(hill_de, text = "Submit", padx = 20 , pady = 10, command = lambda: HillDecode(ciphertext, k1.get(), k2.get(), k3.get(), k4.get())).grid(row = 5, column = 2) 

def KCT_de(ciphertext):
    KCT_de = Toplevel()
    KCT_de.title('Keyed Columnar Transposition Decryption')

    txt = "                    Enter a Keyword to decrypt with                    "
    l = Label(KCT_de, text = txt).grid(row = 0, column = 0, columnspan = 5, padx = 10 , pady = 10)

    key = Entry(KCT_de, width = 10)
    key.grid(row = 1, column = 2)
    keyl = Label(KCT_de, text = "Keyword").grid(row = 2, column = 2)

    sub = Button(KCT_de, text = "Submit", padx = 20 , pady = 10, command = lambda: KCTDecode(ciphertext, key.get())).grid(row = 3, column = 2) 
    
    
def perm_de(ciphertext):
    perm_de = Toplevel()
    perm_de.title("Permutation Decryption")

    def block_perm_de(planetext, bs):
        txt = "                    Enter Block Size                    "
        l = Label(perm_de, text = txt).grid(row = 4, column = 0, columnspan = int(bs), padx = 10 , pady = 10)
        bs_int = int(bs)
        options = []
        number = []

        for i in range(bs_int):
            options.append(i+1)
            number.append(IntVar())

        for i in range(bs_int):
            num = str(i+1)
            drop = OptionMenu(perm_de, number[i], *options)
            drop.grid(row = 5, column = i, padx = 10 , pady = 10)
            bsl = Label(perm_de, text = num).grid(row = 6, column = i)
        l2 = Label(perm_en, text = "(You should not repeat numbers unless you want to loose information)").grid(row = 7, column = 0, columnspan = int(bs), padx = 10 , pady = 10)
        b = Button(perm_de, text = "Submit", command = lambda: PermDecode(ciphertext, number))
        b.grid(row = 7, column = 0 ,columnspan = bs_int, padx = 10 , pady = 10)
    
    txt = "                    Enter Block Size                    "
    l = Label(perm_de, text = txt).grid(row = 0, column = 0, columnspan = 5, padx = 10 , pady = 10)

    bs = Entry(perm_de, width = 10)
    bs.grid(row = 1, column = 2)
    bsl = Label(perm_de, text = "Block Size").grid(row = 2, column = 2)

    sub = Button(perm_de, text = "Next", padx = 20 , pady = 10, command = lambda: block_perm_de(ciphertext, bs.get())).grid(row = 3, column = 2)

def vig_de(ciphertext):
    vig_de = Toplevel()
    vig_de.title("Vienére Decryption")

    txt = "                    Enter a Keyword to decrypt with                    "
    l = Label(vig_de, text = txt).grid(row = 0, column = 0, columnspan = 5, padx = 10 , pady = 10)

    key = Entry(vig_de, width = 10)
    key.grid(row = 1, column = 2)
    keyl = Label(vig_de, text = "Keyword").grid(row = 2, column = 2)

    sub = Button(vig_de, text = "Submit", padx = 20 , pady = 10, command = lambda: VigDecode(ciphertext, key.get())).grid(row = 3, column = 2) 

    
#======================================================================================================
"""

"""

def en_destroy():
    global en
    global init
    init = 0
    en.destroy()

def de_destroy():
    global de
    global init
    init = 0
    de.destroy()

def te_destroy():
    global te
    global init
    init = 0
    te.destroy()

    
#======================================================================================================

"""

"""

def but_en1():
    global init
    init = 1
    
    global en
    de.destroy()
    txt = "Enter your planetext and select type of encryption"
    en = Toplevel()
    en.title('Encrypt')

    
    l = Label(en, text = txt).grid(row = 0, column = 0, columnspan = 7, padx = 10 , pady = 10)
    e = Entry(en, width = 70)
    e.grid(row = 1, column = 0, columnspan = 7, padx = 20, pady = 10)
    e.insert(0, "Enter planetext here")

    button_affine = Button(en, text = "Affine", padx = 20 , pady = 10, command = lambda: aff_en(e.get())).grid(row = 2, column = 1, padx = 10 , pady = 10)
    button_autokey = Button(en, text = "Autokey", padx = 20 , pady = 10, command = lambda: auto_en(e.get())).grid(row = 2, column = 3, padx = 10 , pady = 10)
    button_hill = Button(en, text = "Hill", padx = 20 , pady = 10, command = lambda: hill_en(e.get())).grid(row = 2, column = 5, padx = 10 , pady = 10)
    button_KCT = Button(en, text = "KCT", padx = 20 , pady = 10, command = lambda: KCT_en(e.get())).grid(row = 3, column = 1, padx = 10 , pady = 10)
    button_perm = Button(en, text = "Permutation", padx = 20 , pady = 10, command = lambda: perm_en(e.get())).grid(row = 3, column = 3, padx = 10 , pady = 10)
    button_vig = Button(en, text = "Vigenére", padx = 20 , pady = 10, command = lambda: vig_en(e.get())).grid(row = 3, column = 5, padx = 10 , pady = 10)
    
    button_de = Button(en, text = "Switch to Decrypt", padx = 20 , pady = 10, command = but_de1).grid(row = 4, column = 2, padx = 10 , pady = 10)
    button_exit = Button(en, text = "Go Back", padx = 20 , pady = 10, command = en_destroy).grid(row = 4, column = 4, padx = 10 , pady = 10)
    en.mainloop()


def but_de1():
    global init
    init = 2

    global de
    en.destroy()
    txt = "Enter your ciphertext and select the type of encryption used"
    de = Toplevel()
    de.title('Decrypt')
    l = Label(de, text = txt).grid(row = 0, column = 0, columnspan = 7, padx = 10 , pady = 10)
    e = Entry(de, width = 70)
    e.grid(row = 1, column = 0, columnspan = 7, padx = 20, pady = 10)
    e.insert(0, "Enter ciphertext here")

    button_affine = Button(de, text = "Affine", padx = 20 , pady = 10, command = lambda: aff_de(e.get())).grid(row = 2, column = 1, padx = 10 , pady = 10)
    button_autokey = Button(de, text = "Autokey", padx = 20 , pady = 10, command = lambda: auto_de(e.get())).grid(row = 2, column = 3, padx = 10 , pady = 10)
    button_hill = Button(de, text = "Hill", padx = 20 , pady = 10, command = lambda: hill_de(e.get())).grid(row = 2, column = 5, padx = 10 , pady = 10)
    button_KCT = Button(de, text = "KCT", padx = 20 , pady = 10, command = lambda: KCT_de(e.get())).grid(row = 3, column = 1, padx = 10 , pady = 10)
    button_perm = Button(de, text = "Permutation", padx = 20 , pady = 10, command = lambda: perm_de(e.get())).grid(row = 3, column = 3, padx = 10 , pady = 10)
    button_vig = Button(de, text = "Vigenére", padx = 20 , pady = 10, command = lambda: vig_de(e.get())).grid(row = 3, column = 5, padx = 10 , pady = 10)
    
    button_en = Button(de, text = "Switch to Encrypt", padx = 20 , pady = 10, command = but_en1).grid(row = 4, column = 2, padx = 10 , pady = 10)
    button_exit = Button(de, text = "Go Back", padx = 20 , pady = 10, command = de_destroy).grid(row = 4, column = 4, padx = 10 , pady = 10)
    de.mainloop()


def but_en():
    global init
    global en
    global de
    global te
    global e

    if init == 1:
        response  = messagebox.askyesno("Uh Oh!", "You already have a window open! Close previous window?")

        if response == 1:
            en.destroy()
        elif response == 0:
            return
            
        
    elif init == 2:
        response  = messagebox.askyesno("Uh Oh!", "You already have a window open! Close previous window?")

        if response == 1:
            de.destroy()
        elif response == 0:
            return
        
            
        
    elif init == 3:
        response  = messagebox.askyesno("Uh Oh!", "You already have a window open! Close previous window?")

        if response == 1:
            te.destroy()
        elif response == 0:
            return
    
    init = 1

    txt = "Enter your planetext and select type of encryption"
    en = Toplevel()
    en.title('Encrypt')
    l = Label(en, text = txt).grid(row = 0, column = 0, columnspan = 7, padx = 10 , pady = 10)
    e = Entry(en, width = 70)
    e.grid(row = 1, column = 0, columnspan = 7, padx = 20, pady = 10)
    e.insert(0, "Enter planetext here")


    button_affine = Button(en, text = "Affine", padx = 20 , pady = 10, command = lambda: aff_en(e.get())).grid(row = 2, column = 1, padx = 10 , pady = 10)
    button_autokey = Button(en, text = "Autokey", padx = 20 , pady = 10, command = lambda: auto_en(e.get())).grid(row = 2, column = 3, padx = 10 , pady = 10)
    button_hill = Button(en, text = "Hill", padx = 20 , pady = 10, command = lambda: hill_en(e.get())).grid(row = 2, column = 5, padx = 10 , pady = 10)
    button_KCT = Button(en, text = "KCT", padx = 20 , pady = 10, command = lambda: KCT_en(e.get())).grid(row = 3, column = 1, padx = 10 , pady = 10)
    button_perm = Button(en, text = "Permutation", padx = 20 , pady = 10, command = lambda: perm_en(e.get())).grid(row = 3, column = 3, padx = 10 , pady = 10)
    button_vig = Button(en, text = "Vigenére", padx = 20 , pady = 10, command = lambda: vig_en(e.get())).grid(row = 3, column = 5, padx = 10 , pady = 10)
    
    button_de = Button(en, text = "Switch to Decrypt", padx = 20 , pady = 10, command = but_de1).grid(row = 5, column = 2, padx = 10 , pady = 10)
    button_exit = Button(en, text = "Go Back", padx = 20 , pady = 10, command = en_destroy).grid(row = 5, column = 4, padx = 10 , pady = 10)
    
    en.mainloop()


def but_de():
    global init
    global de
    global en
    global te
    
        
    if init == 1:
        response  = messagebox.askyesno("Uh Oh!", "You already have a window open! Close previous window?")

        if response == 1:
            en.destroy()
        elif response == 0:
            return
            
        
    elif init == 2:
        response  = messagebox.askyesno("Uh Oh!", "You already have a window open! Close previous window?")

        if response == 1:
            de.destroy()
        elif response == 0:
            return
        
            
        
    elif init == 3:
        response  = messagebox.askyesno("Uh Oh!", "You already have a window open! Close previous window?")

        if response == 1:
            te.destroy()
        elif response == 0:
            return

    init = 2
    
    txt = "Enter your planetext and select type of encryption"
    de = Toplevel()
    de.title('Decrypt')
    l = Label(de, text = txt).grid(row = 0, column = 0, columnspan = 7, padx = 10 , pady = 10)
    e = Entry(de, width = 70)
    e.grid(row = 1, column = 0, columnspan = 7, padx = 20, pady = 10)
    e.insert(0, "Enter ciphertext here")

    button_affine = Button(de, text = "Affine", padx = 20 , pady = 10, command = lambda: aff_de(e.get())).grid(row = 2, column = 1, padx = 10 , pady = 10)
    button_autokey = Button(de, text = "Autokey", padx = 20 , pady = 10, command = lambda: auto_de(e.get())).grid(row = 2, column = 3, padx = 10 , pady = 10)
    button_hill = Button(de, text = "Hill", padx = 20 , pady = 10, command = lambda: hill_de(e.get())).grid(row = 2, column = 5, padx = 10)
    button_KCT = Button(de, text = "KCT", padx = 20 , pady = 10, command = lambda: KCT_de(e.get())).grid(row = 3, column = 1, padx = 10 , pady = 10)
    button_perm = Button(de, text = "Permutation", padx = 20 , pady = 10, command = lambda: perm_de(e.get())).grid(row = 3, column = 3, padx = 10 , pady = 10)
    button_vig = Button(de, text = "Vigenére", padx = 20 , pady = 10, command = lambda: vig_de(e.get())).grid(row = 3, column = 5, padx = 10 , pady = 10)
    
    
    button_en = Button(de, text = "Switch to Encrypt", padx = 20 , pady = 10, command = but_en1).grid(row = 4, column = 2, padx = 10 , pady = 10)
    button_exit = Button(de, text = "Go Back", padx = 20 , pady = 10, command = de_destroy).grid(row = 4, column = 4, padx = 10 , pady = 10)
    de.mainloop()


def but_te():
    global init
    global de
    global en
    global te
    
        
    if init == 1:
        response  = messagebox.askyesno("Uh Oh!", "You already have a window open! Close previous window?")

        if response == 1:
            en.destroy()
        elif response == 0:
            return
            
        
    elif init == 2:
        response  = messagebox.askyesno("Uh Oh!", "You already have a window open! Close previous window?")

        if response == 1:
            de.destroy()
        elif response == 0:
            return
        
            
        
    elif init == 3:
        response  = messagebox.askyesno("Uh Oh!", "You already have a window open! Close previous window?")

        if response == 1:
            te.destroy()
        elif response == 0:
            return

    init = 3
    
    txt = "Enter your string select test"
    te = Toplevel()
    te.title('Tests')
    l = Label(te, text = txt).grid(row = 0, column = 0, columnspan = 7, padx = 10 , pady = 10)
    e = Entry(te, width = 70)
    e.grid(row = 1, column = 0, columnspan = 7, padx = 20, pady = 10)
    e.insert(0, "Enter string here")

    button_IOC = Button(te, text = "Index of Coincidence", padx = 20 , pady = 10, command = lambda: IOC(e.get())).grid(row = 2, column = 1, padx = 10 , pady = 10)
    button_Kappa = Button(te, text = "Kappa Test", padx = 20 , pady = 10, command = lambda: Kappa(e.get())).grid(row = 2, column = 3, padx = 10 , pady = 10)
    button_LF = Button(te, text = "Letter Frequency", padx = 20 , pady = 10, command = lambda: LF(e.get())).grid(row = 2, column = 5, padx = 10 , pady = 10)

    button_exit = Button(te, text = "Go Back", padx = 20 , pady = 10, command = te_destroy).grid(row = 4, column = 3, padx = 10 , pady = 10)
    
    
#======================================================================================================

"""

"""

intro = "Welcome to Bosley! Please click a button below to start or 'Exit' to exit."
    
l = Label(root, text = intro).grid(row = 0, column = 0, columnspan = 5, padx = 10 , pady = 10)
button_en = Button(root, text = "Open Encrypter", padx = 20 , pady = 10, command = but_en).grid(row = 1, column = 1, pady = 10)
button_de = Button(root, text = "Open Decrypter", padx = 20 , pady = 10, command = but_de).grid(row = 1, column = 3, pady = 10)
button_te = Button(root, text = "Open Tests", padx = 20 , pady = 10, command = but_te).grid(row = 2, column = 2, pady = 10)
button_exit = Button(root, text = "Exit", padx = 20 , pady = 10, command = root.quit).grid(row = 3, column = 2, pady = 10)


root.mainloop()
