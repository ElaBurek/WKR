#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Nazwa pliku: AES_CTR.py

from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util import Counter

#######------- Niepotrzebne funkcje ustaw jako komentarz

#wektor inicjujący 16B generowany losowo
iv = Random.new().read(16)
iv_hex = iv.encode("hex")
print "iv = %s" %iv_hex

#wektor inicjujący podany w hex
iv_hex = "Tutaj wpisz wektor inicjujący w hex jeśli go nie generujesz"

ctr=Counter.new(128, initial_value=int(iv_hex,16))

def szyfruj(klucz, ctr, tekst):
    #zwraca szyfrogram w hex
    szyfr = AES.new(klucz, AES.MODE_CTR, counter = ctr)
    return (szyfr.encrypt(tekst)).encode("hex")

def deszyfruj(klucz, ctr, szyfrogram):
    #zwraca tekst jawny
    szyfr = AES.new(klucz, AES.MODE_CTR, counter=ctr)
    return szyfr.decrypt(szyfrogram)

#klucz 16B generowany losowo
klucz = Random.new().read(16)
klucz_hex = klucz.encode("hex")
print "klucz = %s" %klucz_hex

#klucz podany w hex
klucz = "Tutaj wpisz klucz w hex jeśli nie generujesz klucza".decode("hex")

#szyfrowanie
tekst = "Tu jest miejsce na Twój tajny tekst"
szyfrogram = szyfruj(klucz, ctr, tekst)
print "%s" %szyfrogram

#deszyfrowanie
#szyfrogram podany w hex
szyfrogram = "Tutaj jest miejsce na tekst zaszyfrowany w hex".decode("hex")
tekst = deszyfruj(klucz, ctr, szyfrogram)
print "%s" %tekst
