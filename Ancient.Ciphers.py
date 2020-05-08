#!/usr/bin/env python3
"""
Description: Ancient implementation of Caesar/ROTxx/Vigenere ciphers.
Author: DrunkenAlcoholic
Date: June 2019
"""

# Custom Alphabet used for Caesar or Vigenre or Both
sAlphabet = 'aBcDeFgHiJkLmNoPqRsTuVwXyZAbCdEfGhIjKlMnOpQrStUvWxYz0123456789'
iAlphaBet = len(sAlphabet)


def caesar(sSource, iShift, bDecrypt = False):

    sResult = ''
    for cChar in sSource:
        try:
            if bDecrypt:
                sResult += sAlphabet[((sAlphabet.index(cChar) + iAlphaBet) - iShift) % iAlphaBet]
            else:
                sResult += sAlphabet[(sAlphabet.index(cChar) + iShift) % iAlphaBet]
        except ValueError:
             sResult += cChar

    return sResult


def vigenere(sSource, sKey, bDecrypt = False, iTableSize = 94):

    # Create a table, can also use custom table(sAlphabet) 
    i = 32
    sTable = ''
    while i < (iTableSize + 32):
        sTable += chr((i))
        i += 1

    # Set key length equal or greater than Source length
    sFinalKey = sKey
    while len(sFinalKey) <= len(sSource):
        sFinalKey += sKey

    # Remove feedline & Carrage return from Source
    for cChar in sSource:
        if (cChar == chr(10)) or (cChar == chr(13)):
            del(sSource[cChar])

    # Vigenere Encrypt / Decrypt
    i = 0
    sResult = ''
    while i <= (len(sSource) -1):
        if sTable.index(sSource[i]) == -1:
            sResult += sSource[i]
        iPosText = sTable.index(sSource[i])
        iPosKey = sTable.index(sFinalKey[i])
        if bDecrypt:
            sResult += sTable[(((iPosText + iTableSize) - iPosKey) % iTableSize)]
        else:
            sResult += sTable[((iPosText + iPosKey) % iTableSize)]
        i += 1

    return sResult + " : " + sTable


# Example Caesar
print("Caesar cipher example")
sInput = input("enter string: ")
iShift = int(input("enter shift number: "))
print("original string: ", sInput)
sCaesar = caesar(sInput, iShift)
print("after cipher: ", sCaesar)
sCaesar = caesar(sCaesar, iShift, True)
print("after decipher: ", sCaesar)
# Example Vigenere
print("\n Vigenere cipher example")
sInput = input("enter string: ")
sInputKey = input("enter key: ")
print("Original String: ", sInput)
sVigenere = vigenere(sInput, sInputKey)
print("after Vigenere cipher: ", sVigenere)
sVigenere =  vigenere(sVigenere, sInputKey, True )
print("after Vigenere decipher: ", sVigenere)
