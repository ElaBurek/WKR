#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Nazwa pliku: md5.py

import hashlib
BLOCKSIZE = 65536
hasher = hashlib.md5()
with open('plik2_2.txt', 'rb') as plik:
    buf = plik.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = plik.read(BLOCKSIZE)
print(hasher.hexdigest())
