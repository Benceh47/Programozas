def listaFeltoltes():
    db = int(input())
    t = []
    for i in range(db):
        sor = input()
        st = sor.split(' ')
        tuple = (st[0],int(st[1]),int(st[2]))
        t.append(tuple)
    return t




# Függvény, ami visszaadja az összes mázsa gyümölcsöt
def osszMennyiseg(adatok):
    ossz = 0
    for adat in adatok:
        ossz += adat[1]
    return ossz


def nagyobbMennyisegDarab(adatok, ertek):
    db = 0
    for adat in adatok:
        if adat[1] > ertek:
            db += 1
    return db


def main():
    adatok = listaFeltoltes()
    print(adatok)
    adat = adatok[2]
    print(adat[0])
    # print(adatok[2][0])
    print("Összesen", osszMennyiseg(adatok), "mázsa gyümölcs van.")
    print("10 mázsánál több gyümölcsből ennyi van:", nagyobbMennyisegDarab(adatok, 10))
main()


#irjon függvényt ami visszaadja az összetett szerkezetből, hogy ősszesen hány mázsa gyümölcs van!!!!!!! második érték a mázsa
#irjon egy függvényt, ami vissza adja a paraméterben megadott értéktől nagyobb összeggel rendelkező gyümölcsök darabszámát!