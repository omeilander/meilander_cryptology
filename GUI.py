# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 19:28:45 2020

@author: omeil
"""

from Master import Encrypt
from Master import Decrypt
from tkinter import *
from tkinter import messagebox

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

def AffineEncode(S, m, n):
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

    close = Button(out, text = "Close", padx = 20 , pady = 10, command = Close).grid(row = 2, column = 2) 


def HillEncode(S, k1, k2, k3, k4):
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

    close = Button(out, text = "Close", padx = 20 , pady = 10, command = Close).grid(row = 2, column = 2)

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

    close = Button(out, text = "Close", padx = 20 , pady = 10, command = Close).grid(row = 2, column = 2)
    

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

    close = Button(out, text = "Close", padx = 20 , pady = 10, command = Close).grid(row = 2, column = 2)
    

#======================================================================================================

"""
Comment
"""

def AffineDecode(S, m, n):
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

    close = Button(out, text = "Close", padx = 20 , pady = 10, command = Close).grid(row = 2, column = 2) 


def HillDecode(S, k1, k2, k3, k4):
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

    close = Button(out, text = "Close", padx = 20 , pady = 10, command = Close).grid(row = 2, column = 2)

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

    close = Button(out, text = "Close", padx = 20 , pady = 10, command = Close).grid(row = 2, column = 2)

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

    close = Button(out, text = "Close", padx = 20 , pady = 10, command = Close).grid(row = 2, column = 2)
    

#=====================================================================================================

"""
Comment
"""
    
def aff_en(planetext):
    aff_en = Toplevel()
    aff_en.title('Affine Encryption')
    
    txt = "Enter a value for m and n where m and n are for the multiplicative and shift ciphers respectivly"
    l = Label(aff_en, text = txt).grid(row = 0, column = 0, columnspan = 5, padx = 10 , pady = 10)
    
    m = Entry(aff_en, width = 10)
    m.grid(row = 1, column = 1)
    ml = Label(aff_en, text = "m").grid(row = 2, column = 1)

    n = Entry(aff_en, width = 10)
    n.grid(row = 1, column = 3)
    nl = Label(aff_en, text = "n").grid(row = 2, column = 3)

    sub = Button(aff_en, text = "Submit", padx = 20 , pady = 10, command = lambda: AffineEncode(planetext, m.get(), n.get())).grid(row = 3, column = 2) 
    
def hill_en(planetext):
    hill_en = Toplevel()
    hill_en.title('Hill Encryption')

    txt = "Enter a k1, k2, k3, and k4 to encrypt using a Hill cipher"
    l = Label(hill_en, text = txt).grid(row = 0, column = 0, columnspan = 5, padx = 10 , pady = 10)

    k1 = Entry(hill_en, width = 10)
    k1.grid(row = 1, column = 1)
    k11 = Label(hill_en, text = "k1").grid(row = 2, column =  1)
    
    k2 = Entry(hill_en, width = 10)
    k2.grid(row = 1, column = 3)
    k21 = Label(hill_en, text = "k2").grid(row = 2, column =  3)
    
    k3 = Entry(hill_en, width = 10)
    k3.grid(row = 3, column = 1)
    k31 = Label(hill_en, text = "k3").grid(row = 4, column =  1)
    
    k4 = Entry(hill_en, width = 10)
    k4.grid(row = 3, column = 3)
    k41 = Label(hill_en, text = "k4").grid(row = 4, column =  3)

    sub = Button(hill_en, text = "Submit", padx = 20 , pady = 10, command = lambda: HillEncode(planetext, k1.get(), k2.get(), k3.get(), k4.get())).grid(row = 5, column = 2) 

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
        b = Button(perm_en, text = "Submit", command = lambda: PermEncode(planetext, number))
        b.grid(row = 7, column = 0 ,columnspan = bs_int, padx = 10 , pady = 10)
    
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
    
    txt = "Enter a value for m and n where m and n are for the multiplicative and shift ciphers respectivly"
    l = Label(aff_de, text = txt).grid(row = 0, column = 0, columnspan = 5, padx = 10 , pady = 10)
    
    m = Entry(aff_de, width = 10)
    m.grid(row = 1, column = 1)
    ml = Label(aff_de, text = "m").grid(row = 2, column = 1)

    n = Entry(aff_de, width = 10)
    n.grid(row = 1, column = 3)
    nl = Label(aff_de, text = "n").grid(row = 2, column = 3)

    sub = Button(aff_de, text = "Submit", padx = 20 , pady = 10, command = lambda: AffineDecode(ciphertext, m.get(), n.get())).grid(row = 3, column = 2) 
    
def hill_de(ciphertext):
    hill_de = Toplevel()
    hill_de.title('Hill Decryption')

    txt = "Enter a k1, k2, k3, and k4 to encrypt using a Hill cipher"
    l = Label(hill_de, text = txt).grid(row = 0, column = 0, columnspan = 5, padx = 10 , pady = 10)

    k1 = Entry(hill_de, width = 10)
    k1.grid(row = 1, column = 1)
    k11 = Label(hill_de, text = "k1").grid(row = 2, column =  1)
    
    k2 = Entry(hill_de, width = 10)
    k2.grid(row = 1, column = 3)
    k21 = Label(hill_de, text = "k2").grid(row = 2, column =  3)
    
    k3 = Entry(hill_de, width = 10)
    k3.grid(row = 3, column = 1)
    k31 = Label(hill_de, text = "k3").grid(row = 4, column =  1)
    
    k4 = Entry(hill_de, width = 10)
    k4.grid(row = 3, column = 3)
    k41 = Label(hill_de, text = "k4").grid(row = 4, column =  3)

    sub = Button(hill_de, text = "Submit", padx = 20 , pady = 10, command = lambda: HillDecode(ciphertext, k1.get(), k2.get(), k3.get(), k4.get())).grid(row = 5, column = 2) 

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

    
    l = Label(en, text = txt).grid(row = 0, column = 0, columnspan = 5, padx = 10 , pady = 10)
    e = Entry(en, width = 70)
    e.grid(row = 1, column = 0, columnspan = 5, padx = 20, pady = 10)

    button_affine = Button(en, text = "Affine", padx = 20 , pady = 10, command = lambda: aff_en(e.get())).grid(row = 2, column = 1)
    button_hill = Button(en, text = "Hill", padx = 20 , pady = 10, command = lambda: hill_en(e.get())).grid(row = 2, column = 3)
    button_perm = Button(en, text = "Permutation", padx = 20 , pady = 10, command = lambda: perm_en(e.get())).grid(row = 3, column = 1)
    button_vig = Button(en, text = "Vigenére", padx = 20 , pady = 10, command = lambda: vig_en(e.get())).grid(row = 3, column = 3)
    
    button_de = Button(en, text = "Switch to Decrypt", padx = 20 , pady = 10, command = but_de1).grid(row = 4, column = 1)
    button_exit = Button(en, text = "Go Back", padx = 20 , pady = 10, command = en_destroy).grid(row = 4, column = 3)
    en.mainloop()


def but_de1():
    global init
    init = 2

    global de
    en.destroy()
    txt = "Enter your ciphertext and select the type of encryption used"
    de = Toplevel()
    de.title('Decrypt')
    l = Label(de, text = txt).grid(row = 0, column = 0, columnspan = 5, padx = 10 , pady = 10)
    e = Entry(de, width = 70)
    e.grid(row = 1, column = 0, columnspan = 5, padx = 20, pady = 10)

    button_affine = Button(de, text = "Affine", padx = 20 , pady = 10, command = lambda: aff_de(e.get())).grid(row = 2, column = 1)
    button_hill = Button(de, text = "Hill", padx = 20 , pady = 10, command = lambda: hill_de(e.get())).grid(row = 2, column = 3)
    button_perm = Button(de, text = "Permutation", padx = 20 , pady = 10, command = lambda: perm_de(e.get())).grid(row = 3, column = 1)
    button_vig = Button(de, text = "Vigenére", padx = 20 , pady = 10, command = lambda: vig_de(e.get())).grid(row = 3, column = 3)
    
    button_en = Button(de, text = "Switch to Encrypt", padx = 20 , pady = 10, command = but_en1).grid(row = 4, column = 1)
    button_exit = Button(de, text = "Go Back", padx = 20 , pady = 10, command = de_destroy).grid(row = 4, column = 3)
    de.mainloop()


def but_en():
    global init
    global en
    global de
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
    
    init = 1

    txt = "Enter your planetext and select type of encryption"
    en = Toplevel()
    en.title('Encrypt')
    l = Label(en, text = txt).grid(row = 0, column = 0, columnspan = 5, padx = 10 , pady = 10)
    e = Entry(en, width = 70)
    e.grid(row = 1, column = 0, columnspan = 5, padx = 20, pady = 10)


    button_affine = Button(en, text = "Affine", padx = 20 , pady = 10, command = lambda: aff_en(e.get())).grid(row = 2, column = 1)
    button_hill = Button(en, text = "Hill", padx = 20 , pady = 10, command = lambda: hill_en(e.get())).grid(row = 2, column = 3)
    button_perm = Button(en, text = "Permutation", padx = 20 , pady = 10, command = lambda: perm_en(e.get())).grid(row = 3, column = 1)
    button_vig = Button(en, text = "Vigenére", padx = 20 , pady = 10, command = lambda: vig_en(e.get())).grid(row = 3, column = 3)
    
    button_de = Button(en, text = "Switch to Decrypt", padx = 20 , pady = 10, command = but_de1).grid(row = 5, column = 1)
    button_exit = Button(en, text = "Go Back", padx = 20 , pady = 10, command = en_destroy).grid(row = 5, column = 3)
    
    en.mainloop()


def but_de():
    global init
    global de
    global en
    
        
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
        

    init = 2
    
    txt = "Enter your planetext and select type of encryption"
    de = Toplevel()
    de.title('Decrypt')
    l = Label(de, text = txt).grid(row = 0, column = 0, columnspan = 5, padx = 10 , pady = 10)
    e = Entry(de, width = 70)
    e.grid(row = 1, column = 0, columnspan = 5, padx = 20, pady = 10)

    button_affine = Button(de, text = "Affine", padx = 20 , pady = 10, command = lambda: aff_de(e.get())).grid(row = 2, column = 1)
    button_hill = Button(de, text = "Hill", padx = 20 , pady = 10, command = lambda: hill_de(e.get())).grid(row = 2, column = 3)
    button_perm = Button(de, text = "Permutation", padx = 20 , pady = 10, command = lambda: perm_de(e.get())).grid(row = 3, column = 1)
    button_vig = Button(de, text = "Vigenére", padx = 20 , pady = 10, command = lambda: vig_de(e.get())).grid(row = 3, column = 3)
    
    button_en = Button(de, text = "Switch to Encrypt", padx = 20 , pady = 10, command = but_en1).grid(row = 4, column = 1)
    button_exit = Button(de, text = "Go Back", padx = 20 , pady = 10, command = de_destroy).grid(row = 4, column = 3)
    de.mainloop()

    
#======================================================================================================

"""

"""

intro = "Welcome to Bosley! Please click a button below to start or 'Exit' to exit."
    
l = Label(root, text = intro).grid(row = 0, column = 0, columnspan = 5, padx = 10 , pady = 10)
button_en = Button(root, text = "Open Encrypter", padx = 20 , pady = 10, command = but_en).grid(row = 1, column = 1)
button_de = Button(root, text = "Open Decrypter", padx = 20 , pady = 10, command = but_de).grid(row = 1, column = 3)
button_exit = Button(root, text = "Exit", padx = 20 , pady = 10, command = root.quit).grid(row = 2, column = 2)


root.mainloop()
