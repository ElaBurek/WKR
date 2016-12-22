#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Nazwa pliku: meet_in_the_middle.py

import gmpy2
from gmpy2 import mpz
from gmpy2 import powmod
from gmpy2 import f_mod
from gmpy2 import mul

p = mpz(13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171)
h = mpz(4476678147226155115558365457750475595861521772603596936757528326067178243549776543712192144627870184928567432208656624794079113374237487568153440925199271)
g = mpz(26790476600736210439911326117339978371955050182095051707060863109260114006743503487596200818701323671541681934177621901008556022090467034705794892743945893)
Y = 2**20

tab={}

for i in range(Y):
#h/g^x1 (mod p) = h*g^(-x1) (mod p)
#r1 = h (mod p)
#r2 = g^(-x1) (mod p)
#h*g^(-x1) (mod p) = r1*r2 (mod p)
    x1 = i
    r1 = f_mod(h, p)
    r2 = powmod(g, (-x1), p)
    k = mul(r1,r2)
    kk = f_mod(k,p)
    tab[kk]=x1

for i in range(len(tab)):
    x0 = i
    e = x0*Y
    s = powmod(g,e,p)
    if tab.has_key(s) == True:
        break
x1 = tab[s]
x = x0*Y+x1
print "x = %s" %x
