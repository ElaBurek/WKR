#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Nazwa pliku: RSA.py

from Crypto.PublicKey import RSA
from Crypto import Random

generator = Random.new().read
klucz = RSA.generate(1024, generator)

klucz_publiczny = klucz.publickey().exportKey()
klucz_prywatny = klucz.exportKey('PEM', passphrase=None, pkcs=8)
#exportKey(self, format='PEM', passphrase=None, pkcs=1)
#'PEM' - kodowanie tekstowe, kodowanie base64
#pkcs - 1-PKSC#1, 8-PKCS#8

plik1 = open('burek_k_publiczny.pem', 'w')
plik1.write(klucz_publiczny)
plik1.close()
plik2 = open('burek_k_prywatny.pem', 'w')
plik2.write(klucz_prywatny)
plik2.close()

#szyfrowanie
plik3 = open('klucz_olga.pem', 'r')
klucz_olga = RSA.importKey(plik3.read())
plik4 = open('tekst_jawny.txt', 'r')
tekst = plik4.read()
tekst_kod = klucz_olga.encrypt(tekst, 32)
tekst_kod = tekst_kod[0]
plik5 = open('szyfrogram.txt', 'w')
plik5.write(tekst_kod.encode('hex'))
plik3.close()
plik4.close()
plik5.close()

#deszyfrowanie
#plik9 = open('plik_z_kluczem_prywatnym.pem', 'r')
#klucz_priv = RSA.importKey(plik9.read())
#plik10 = open('plik_z_szyfrogramem.txt', 'r')
#szyfr = plik10.read()
#szyfr2 = szyfr.decode('hex')
#message = klucz_priv.decrypt(szyfr2)

#print message

#plik9.close()
#plik10.close()


