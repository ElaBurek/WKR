#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Nazwa pliku: AES_ECB.py

from Crypto.Cipher import AES
from Crypto import Random

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[0:-ord(s[-1])]

def szyfruj(klucz, tekst):
    #zwraca szyfrogram w hex
    tekst = pad(tekst)
    szyfr = AES.new(klucz, AES.MODE_ECB)
    return (szyfr.encrypt(tekst)).encode("hex")

def deszyfruj(klucz, szyfrogram):
    #zwraca tekst jawny
    szyfr = AES.new(klucz, AES.MODE_ECB)
    return unpad(szyfr.decrypt(szyfrogram))

#######------- Niepotrzebne funkcje ustaw jako komentarz

#klucz 16B generowany losowo
klucz = Random.new().read(16)
klucz_hex = klucz.encode("hex")
print "klucz = %s" %klucz_hex

#klucz podany w hex
klucz = "Tutaj wpisz klucz w hex jeśli nie generujesz klucza".decode("hex")

#szyfrowanie
tekst = "Tutaj jest miejsce na Twoją tajną wiadomość"
szyfrogram = szyfruj(klucz, tekst)
print "%s" %szyfrogram

#deszyfrowanie
#szyfrogram podany w hex
szyfrogram = "Tutaj jest miejsce na tekst zaszyfrowany w hex".decode("hex")
tekst = deszyfruj(klucz, szyfrogram)
print "%s" %tekst
