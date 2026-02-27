# Hf - szeleromu.txt
    # telepules, vármegye, tájolás, hány darab szélerőmű, szélerőművenkénti teljesítmény kw/h, mikor telepítették
    # Magyarországon hány szélerőmű van?
    # Írjuk ki, hogy melyik településen és melyik évben telepítették a legtöbb szélerőművet
    # Kérjünk be egy települést! Nézzük meg, hogy van-e ott szélerőmű (pl.: Cegléd: nincs)

def adatokBeolvasasa():
    lista = []
    db = int(input())
    for i in range(db):
        st = input().split(';')
        lista.append((st[0],st[1],st[2],int(st[3]), int(st[4]), int(st[5])))
    return lista

def szeleromumvekDarab(lista):
    osszeg = 0
    for i in range(0,len(lista),1):
        osszeg += lista[i][3]
    return osszeg

def maximumIndexDb(lista):
    maxi = 0
    for i in range(0,len(lista),1):
        if lista[i][3] > lista[maxi][3]:
            maxi = i
    return maxi

def telepulesenVanSzeleromu(lista, telepules):
    i = 0
    while i < len(lista) and lista[i][0] != telepules:
        i += 1
    return i < len(lista)
    

def main():
    t = adatokBeolvasasa()
    #print(t)

    db = szeleromumvekDarab(t)
    print(db, "Darab szélerőmű van Magyarországon")

    maxIndex = maximumIndexDb(t)
    print(t[maxIndex][0], "városban", t[maxIndex][5], "évben telepítették a legtöbb szélerőművet")

    telepules = input("Kérem adja meg a település nevét: ")
    if telepulesenVanSzeleromu(t, telepules):
        print("Van szélerőmű a településen")
    else:
        print("Nincs szélerőmű a településen")
       
    # 2013 május digit kult emelt prog
    # szavazatok.txt
    # http://informatika.fazekas.hu/erettsegi/emelt-szintu-feladatok/
main()
