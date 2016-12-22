#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Nazwa pliku: crip_drag.py

s1 = "56232e8cede71121d5b30365423401b094d57e59e982374d0f122ba50dc4587ec4436206874f21235a29667099d79e9e67052dfc8650fefdf865e867b99765ebc91bdb277b47663a5b4b"
s2 = "5c769e79e7ef0f6fd2b903404d82f9bf8ec069bd0edb82bd551835a511c2566c8b52295adfabd9774c31c09a7a10df9d7d1d3ffb875eeab0b750459bb58a65f4c9169a1e675267325b16f9ee849d9732467de2ae9c81c78288a4156fba61a9ed94c751630dba651088673697259336e9b0"
s3 = "56232e8cede71121d5b303405a280cb083d56ebc09db88b856168a071a8bf6b79d1132509300263e4d2d77797a10dfc978033ff42a94f0f3bd"
s4 = "4b3f8e7dfce3078a3ef854104d2b1eb686c16412e29e98ef581423e91687137894139eb7931525775d3f6a729efb9e9961abc7fc87e302b0a85d4791b43db3ee82a87e5b29566b85bc45e1f08b9cde3a467af9bc9e2c2ad13e4fbe81fb6da0f39eda5787e1f5781e95762a9223853bbcee9da8436acddf00608d3dd3e61f411c2a2948881d3cb8b34a65b535aa73c5a045705375"
s5 = "4c338c61a6e91536cfac465e5c2216f185d6c2fbab9494a64c183da534c4456a87017715d81b83e45c312568351ac4806d033f526b07fdf1b55be97cb18961f78009db136606722f5a0af4f780949173156ae1a78ac96d4d34451379f5"
s6 = "5239cb64e3ef096fd3ba515146285bab868f7710ee8985bc55046fe61ac7136494172954d0052979"
s7 = "452c8e7dede14629c9b64853422815b095c6720af1db82a00f1626e914de13668d17285c77ea23364d20257b33ba272cb40437f28307e3fcb9125b3a5b8a72f68b15db077b4761391e1ff7e99789873907db22a5962c2ad13e4fbe81fb78e2d33539593103b82b0dda7b3b23ff8037fbf137130c76cbd60a799821dfa50d001c2127502fe668b4bd052df628e57a6b4d4f69423aad68567500333806a5e58c"
s8 = "4d399d6fe5fb4620d8a84c4741221fab8ecec2fba7db37734a5d38a505ca406a80083250931b2f775d3c77792904d0806d4f2dfe2dbea7fead565697f2de74e0850794576a49223057a113ed8098de3e136df1eb949cd89e3a47be9ffb72b74173cb513408bc600b8d796f83369721f7f797a8566fc3d013689e73daea141b18372454c4"
s9 = "5237cb74a6f80935d3aa56104526be53888f7d17ea98880baa1e2ea516c55564961f3a56d90e603845297f799ffcdfc97b069a0ec945fe545f125c8cbf8964e3801b3ff229566732fbe7521cc5979232467de2ae9c81c78288a4156fba61a9ed94c751630dba651088673697259336e9b0"
s10 = "452c8e7defa81126d9bc59594d2b12fdc76abb1cab8cd2bf46b9caf114c2136f8b520b47d20829775e3a7f61301b7b556caae2f6c94cf2e2b1575edea4de70f68a168fb38c0666394e09f9f4848787301c705c4ed1c9f29f2c450073b222b2f13422552c11bb620f9b301a8a3f8833efe48ba8437bccd20a79969628fc5b41a9e43611881d8c54f2446250fba029c4aa51650a21088b176c49262747acf9d12240d0999ba808a80dfd25c48751b2afda785d9f64d94bcfcbd0556bd9d85e35c0e5fa81f7e952b7da3b2a7438b86a5dde60bda8c526e5d6b376d0cb"

def xoruj_ss(c1,c2):
    wynik = ""
    i = 0
    while (i < len(c1)):
        a = c1[i:(i+2)]
        b = c2[i:(i+2)]
        a_d = int(a,16)
        b_d = int(b,16)
        axb = a_d^b_d
        axb_h1 = hex(axb)
        axb_h = axb_h1[2:len(axb_h1)]
        if ((len(axb_h)%2) != 0):
            axb_h = '0' + axb_h
        wynik = wynik + axb_h
        i = i+2
    return wynik

slowo = "Tutaj wpisz słowo lub zdanie, które może wystąpić w szyfrogramie"
slowo_h = slowo.encode("hex")

#wstaw odpowiednie szyfrogramy do xorowania
szyfr1 = s1
szyfr2 = s2

#przycinanie szyfrogramów do rownej dlugosci
if (len(szyfr1) > len(szyfr2)):
    szyfr1 = szyfr1[:len(szyfr2)]
else:
    szyfr2 = szyfr2[:len(szyfr1)]

ss = xoruj_ss(szyfr1,szyfr2)

#przycinanie do dlugosci slowa, zaczynając od pozycji "i" w szyfrogramie (numeracja od 0)
i = 0
ss_c = ss[i:(i+len(slowo_h))]

tekst = xoruj_ss(ss_c, slowo_h)
    
tekst_str = tekst.decode("hex")
print tekst_str

#---------- WYZNACZENIE KLUCZA

wiadomosc = "Tutaj wpisz rozszyfrowaną wiadomość"
wiadomosc_h = wiadomosc.encode("hex")

#Wpisz odpowiadający jej szyfrogram
szyfr = s10

#przycinanie do rownej dlugosci
if (len(szyfr) > len(wiadomosc_h)):
    szyfr = szyfr[:len(wiadomosc_h)]
else:
    wiadomosc_h = wiadomosc_h[:len(szyfr)]

klucz = xoruj_ss(szyfr, wiadomosc_h)
klucz_str = klucz.decode("hex")

print klucz_str

#----------- ODSZYFROWANIE DODATKOWEGO SZYFROGRAMU NA PODSTAWIE KLUCZA

s14 = "56232e8cede71121d5b3035debf41c14658f6b10f88f8bef5d1235f6066eb16a20f57b4f93182932423d2575331bd49a6b4f2cf89354eef1b64b4f96fe8e6fb98a0d3ef56c4c222f550afaf0868ad2730bdd2bac3a6b88952c511bdc5c22a8e1d1c4516311ac78a1787121892dd221ebf198ed4621d2dc026c9d9019f214044c3b2948ca1732bcb44c7ffa30ac258ea2f5b94d9eebcf1d6e5520301e021b823f40d8818ebf0b044b1b6bc28002b9b4c8725d33a56881db8fd04363dec9f0a6c3b7f781e2e6b650d78cd23b5bb27d44cf68a119283ef373573cca8c3daa624b6be37851abba2e384e18627690e1364778e4e908ea247c3e76"

#przycinanie do rownej dlugosci
if (len(s14) > len(klucz)):
    s14 = s14[:len(klucz)]
else:
    klucz = klucz[:len(s14)]

m14 = xoruj_ss(klucz,s14)

m14_str = m14.decode("hex")
print m14_str
