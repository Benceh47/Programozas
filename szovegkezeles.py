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
    szorzat = ord(nev[0]) * ord(nev[1]) * ord(nev[2])
elif hossz == 2:
    szorzat = ord(nev[0]) * ord(nev[1]) * hossz
elif hossz == 1:
    szorzat = ord(nev[0]) * hossz * hossz * hossz
else:
    szorzat = 0
print("a jelszava: " + str(szorzat))
