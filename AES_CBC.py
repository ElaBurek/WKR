#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Nazwa pliku: AES_CBC.py

from Crypto.Cipher import AES
from Crypto import Random

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[0:-ord(s[-1])]

def szyfruj(klucz, iv, tekst):
    #zwraca szyfrogram w hex
    tekst = pad(tekst)
    szyfr = AES.new(klucz, AES.MODE_CBC, iv)
    #return (iv + szyfr.encrypt(tekst)).encode("hex")
    return (szyfr.encrypt(tekst)).encode("hex")

def deszyfruj(klucz, iv, szyfrogram):
    #zwraca tekst jawny
    szyfr = AES.new(klucz, AES.MODE_CBC, iv)
    return unpad(szyfr.decrypt(szyfrogram))

#######------- Niepotrzebne funkcje ustaw jako komentarz

#klucz 16B generowany losowo
klucz = Random.new().read(16)
klucz_hex = klucz.encode("hex")
print "klucz = %s" %klucz_hex

#klucz podany w hex
klucz = "Tutaj wpisz klucz w hex jeśli nie generujesz klucza".decode("hex")

#wektor inicjujący 16B generowany losowo
iv = Random.new().read(16)
iv_hex = iv.encode("hex")
print "iv = %s" %iv_hex

#wektor inicjujący podany w hex
iv = "Tutaj wpisz wektor inicjujący w hex jeśli go nie generujesz".decode("hex")

#szyfrowanie
tekst = "Tu jest miejsce na Twój tajny tekst"
szyfrogram = szyfruj(klucz, iv, tekst)
print "%s" %szyfrogram

#deszyfrowanie
#szyfrogram podany w hex
szyfrogram = "Tutaj jest miejsce na tekst zaszyfrowany w hex".decode("hex")
tekst = deszyfruj(klucz, iv, szyfrogram)
print "%s" %tekst
