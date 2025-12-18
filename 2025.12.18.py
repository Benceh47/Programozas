"""
Utasitás(szekvencia)
-menj előre
-fordulj
-szivd be a levegőt
-fújd ki a levegőt
- ...
-Irasd ki - print()
-tárold el - változonév= érték
-számold ki - változonév = <Képlet>
-kérd be - input("add meg:")


Elágazás - (szelekció)
-Ha piros a lámpa akkor megállok
-Ha zöld a lámpa akkor elindulok
Ha fal van elöttem elfordulok
Ha tudom hogy nem megy akkor gyakorlom
...
Ha a bekért szám páros akkor kiirom hogy páros különben kiiratom, hogy páratlan
Ha a dobokocka értéke 5 akkor előre lépek 5-öt
ismétlés ciklu (iteráció)
-Addig menj amig a tábla an
-ADdig dobáld az aprot a gépbe amig el nem éred az össezeget
- Üss bele 3db tojást
-Addig tegyél bele cukrot amig elég édes nem lett
-Addig gyakorlok amig meg nem értem
- Addig fog a tanár piszkálni amig nem látja hogy értem.
"""

db = 12
print("szám:", db)
#a szám utolso számjegye páros-e?
utolso_szamjegy = db % 10
print("utolsó számjegy:", utolso_szamjegy)

if(utolso_szamjegy % 2 ==0):
    print("páros")
else:
    print("páratlan")


    #db-nyi almát szeretnék látni
for kiskutya in range(2,db,3):
    print(kiskutya+1,"Alma")


szoveg= "kalapács"
print(szoveg)
index = 0
for karakter in szoveg:
    index+=1
    print(index,karakter)

