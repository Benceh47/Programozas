"""
Függvények
(Scratch blokkok)

Előre definált(megirt) folyamatok, amik a külsö értéktől függöen végrehajtják a belső utasitásokat


Def fuggvenyNev:
    #függvény tartalma

fuggvenyNev() #függvény meghivása
"""
import random

#összeadás függvény definálása
def osszeadas():
    a=12
    b=17
    print(a+b)

#osszeadas kulso ertektol függöen PARAMÉTEREN keresztül
def osszeadasParam(a,b):
    c = a + b
    print(c)
#osszeadas függvény meghivása
osszeadas()
osszeadasParam(12,17)

def kettoAtizediken():
    #a = math.power(2,10)
    a = 2**10
    return a

valtozo = kettoAtizediken()
print(valtozo)

def osszeadasVisszateressel(a,b):
    c = a + b
    return c
print(osszeadasVisszateressel(30,37))

#definálj egy olyan eljárás nem tér vissza értékkel, aminek a paraméterébe bekerül egy darabszám és a függvény pedig kiir ennyi darab véletlen számot egymás mellé!

def veletlenszamkiiratas(db):
    for i in range(0,db,1):
        print(random.randint(100,999),end=" ")

veletlenszamkiiratas(5)

print()
#készitsen egy eljárást ami függ egy szövegtől és kiirja a szót visszafele

def szovisszafele(szoveg):
    for index in range(len(szoveg)-1,-1,-1):
        print(szoveg[index], end="")
    print()
szovisszafele("TamasMadeIt BEAT!!!!!!!! készitő 10k a bevétel ami jó de még nem kapta meg a pénzt +- 10k")


def szovisszafeletwo(szoveg):
    ferdepaci= ""
    for index in range(len(szoveg)-1,-1,-1):
        ferdepaci+=szoveg[index]
    return(ferdepaci)
print(szovisszafeletwo("tamas egy papucs is egybe meg fars és link és ratyi szerelő"))

print()
#irjon egy fv-t ami egy szórol eldönti hogy palindrom-e? és vissza adja válaszul(visszafele ugyan az)
def palindrom(szo):
#     s = ""
#     for karakter in szo:
#         if karakter != " ":
#             s += karakter
#     if s == s[::-1]:
#         print("palindrom")
#     else:
#         print("nem palindrom")
# palindrom("tamas anyjaba szerelmes vagyok")

    if(szo == szovisszafeletwo(szo)):
        return True
    else:
        return False
print("gereb vereb timi tomi berev bereg merev kereb csitra articika katicir atcsi erek verme gereb veri keri nyali fali mali silaf inek pinek pita fika")
print("palindrom-e a szó:",palindrom("gereb vereb timi tomi berev bereg merev kereb csitra articika katicir atcsi erek verme gereb veri keri nyali fali mali silaf inek pinek pita fika"))

#készitsen egy függvényt ami egy db számtol függ és vissza ad   
#egy feltöltött listát [10,50] közötti számokkal

def tamaslista(db):
    lista = []
    for i in range(0,db,1):
        lista.append(random.randint(-10,50))
    return(lista)
print(tamaslista(19))