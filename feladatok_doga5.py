Mentse a programot Monogramja_doga5.py néven a H:/ meghajtó gyökér könyvtárába!
Shrek és Fióna kiruccannak a Kacifánt Kaszinóba kockázni. Két darab 18 oldalú kockával 
dobnak, ahol a számok 1-18ig vannak. A játékosok egymás után dobják a két kockát egyszerre
és felírják a saját lapjukra egymás után a kidobott értékek összegét. A játék 7 körös és utána 
derül ki, hogy ki nyert vagy esetleg a játék eredménye döntetlen. Fióna kezdi mindig a játékot.
A nyertes a 7 kör kidobott összege alapján dől el.
Írjon programot, ami szimulálja Shrek és Fióna játékát a következő pontok alapján! Az 
eljárások, függvények nevét szabadon kitalálhatja házi rendnek megfelelő szabályok alapján!
1. Írjon egy függvényt, ami visszatér egy olyan listával, ami paraméterként megkap egy 
darabszámot és a feladatban leírtak alapján kigenerál annyi véletlen számot! Majd 
hozzon létre két listát felhasználva a függvényt a feladatban megadott darabszámmal! 
Ha nem sikerült megírnia a függvényt, akkor használja a következő két listát:
Shrek: [31,20,12,22,34,4,7]
Fióna: [9,19,2,2,22,14,6]
2. Írjon egy függvényt, ami megadja egy lista elemeinek összegét!
3. Írjon egy eljárást, ami a mintának megfelelően kiíratja egy lista elemeit és összegét. A 
folyamatnak függenie kell egy listától és a lista összegétől!
4. Írjon egy függvényt, ami megadja, hogy a játékot ki nyert! Shrek, Fióna vagy Döntetlen 
lehet a kimenetel! Írassa ki a mintának megfelelően!
5. Írjon egy függvényt, ami megadja, hogy volt-e olyan kör, amikor mindkét játékos ugyan 
azt a számot dobta! Mindkét játékos dobására szükség van a függvényben! A mintának 
megfelelően írja ki az eredményt!
+ extra feladat – plusz pontért!
6. Írjon egy függvényt, ami megadja, hogy melyik volt a legkisebb kidobott érték a játék 
során, és azt ki dobta ki és melyik körben? ( Ha tud, akkor ebben a függvényben 
használjon minden információ lekérésére külön függvényt!

import random

def ListaFeltoltes(darabszam):
    lista = []
    for i in range(0, darabszam, 1):
        # 2 db 18 oldalú kocka dobásainak összege 2-től 36-ig terjedhet
        dobas = random.randint(1, 18) + random.randint(1, 18)
        lista.append(dobas)
    return lista

def ListaOsszeg(lista):
    osszeg = 0
    for i in range(0,len(lista),1):
        osszeg += lista[i]
    return osszeg

def ListaKiir(lista,osszeg):
    for i in range(0,len(lista),1):
        print(lista[i],end=" ")
    print("\nÖsszeg:",osszeg)

def JatekNyertese(shrek,fiona):
    if(shrek>fiona):
        print("Shrek nyert!")
    elif(fiona>shrek):
        print("Fiona nyert!")
    else:
        print("Döntetlen!")

def EgyformaDobas(shrek,fiona):
    for i in range(0,len(shrek),1):
        if(shrek[i] == fiona[i]):
            print("Volt olyan kör, amikor mindkét játékos ugyan azt a számot dobta!")
            return
    print("Nem volt olyan kör, amikor mindkét játékos ugyan azt a számot dobta!")

def LegkisebbDobas(shrek,fiona):
    legkisebb = shrek[0]
    jatekos = "Shrek"
    kor = 1
    for i in range(0,len(shrek),1):
        if(shrek[i]<legkisebb):
            legkisebb = shrek[i]
            jatekos = "Shrek"
            kor = i+1
        if(fiona[i]<legkisebb):
            legkisebb = fiona[i]
            jatekos = "Fiona"
            kor = i+1
    print("A legkisebb dobás:",legkisebb,"-t dobta",jatekos,"a",kor,". körben.")

def main():
    shrek = ListaFeltoltes(7)
    fiona = ListaFeltoltes(7)
    print("Shrek dobásai:")
    ListaKiir(shrek,ListaOsszeg(shrek))
    print("Fiona dobásai:")
    ListaKiir(fiona,ListaOsszeg(fiona))
    JatekNyertese(ListaOsszeg(shrek),ListaOsszeg(fiona))
    EgyformaDobas(shrek,fiona)
    LegkisebbDobas(shrek,fiona)
main()