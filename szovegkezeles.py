import random
# 1 lebegőpontos - float - tört
#a = 1.25
#b = float(input("adjon meg egy tizedes törtet: "))
#print(b*4)

# generáljon ki [1.10[ közötti tört számot kettő tizedesjegyre pontossággal

#c=float(random.randint(100,999)/100)
#print(c) 
#hf random.random befejezése
#c = random.random() * 9 + 1    
#c = round(c, 2) 
#print(c)

szoveg = input("adjon meg egy szöveget: ")
print(szoveg)
print("a szöveg hossza: ", len(szoveg)),
print("első karakger",szoveg[0])
#szöveg karakterekből épül fel
# szöveg = karakter lánc
karakter = szoveg[0]
kod = ord(szoveg[0])
print(kod)
ujkod = kod + 1
ujkarakter = chr(ujkod)
print(ujkarakter)

a = chr(random.randint(97, 122))
b = chr(random.randint(97, 122))
c = chr(random.randint(97, 122))
print(a,b,c)

#kérje a felhasználó keresztnevét! Generáljon neki egy jelszót,
#az első 3 karakterének ascii kódjának szorzatát! ha nincs a név, 3jegyű akkor kettő esetén hossz érték legyen a szorzat 3. tagja 1 esetén pedig a szám köbe legyen.
nev = input("adja meg a keresztnevét: ")
hossz = len(nev)
if hossz >= 3:
    kod1 = ord(nev[0])
    kod2 = ord(nev[1])
    kod3 = ord(nev[2])
    jelszo = kod1 * kod2 * kod3     
elif hossz == 2:
    kod1 = ord(nev[0])
    kod2 = ord(nev[1])
    jelszo = kod1 * kod2 * hossz
else:
    kod1 = ord(nev[0])
    jelszo = kod1 * (hossz ** 3)
print("a jelszava:", jelszo)

#kérjén be egy felhasználottol egy számot majd irja ki a szám 13szorosát
szam= int(input("adjon meg egy számot: "))
szam13 = szam * 13
print("a szám 13szorosa:", szam13)
#kérjen be egy szöveget és egy számot majd irja ki a szöveget annyiszor




#genráljon ki egy véletlen kisbetűs karaktert
karakter = chr(random.randint(97, 122))
print(karakter)
szoveg = input("adjon meg egy szöveget: ")
szam = int(input("adjon meg egy számot: "))
for i in range(szam):
    print(szoveg)
#kérjen be egy szöveget és irja ki a szöveg közepén lévő karaktert
szoveg = input("adjon meg egy szöveget: ")
hossz = len(szoveg)
kozep = hossz // 2
print("a szöveg középső karaktere:", szoveg[kozep])
#ha páros a hossz akkor a két középső karaktert
if hossz % 2 == 0:
    print("a szöveg középső karakterei:", szoveg[kozep - 1], szoveg[kozep])
#ha páratlan akkor az egy középső karaktert
else:
    print("a szöveg középső karaktere:", szoveg[kozep])
#kérjen be egy szöveget és irja ki a szöveg fordítottját
szoveg = input("adjon meg egy szöveget: ")
forditott = ""
for i in range(len(szoveg) - 1, -1, -1):
    forditott += szoveg[i]
print("a szöveg fordítva:", forditott)
            
  
