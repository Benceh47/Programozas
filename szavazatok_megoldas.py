
def listaFeltoltes():
    lista = []
    db = int(input())
    for i in range(db):
        st = input().split(' ')
        lista.append((int(st[0]), int(st[1]), st[2], st[3],st[4]))
    return lista

def feladat3(adatok):
    vezeteknev = input("Adja meg a vezetéknevet: ")
    keresztnev = input("Adja meg a keresztnevet: ")
    #nev = input("Adjam egy teljes nevét szóközzel elválasztva: ").split(" ")
    # nev[0] - vezeteknev, nev[1] - keresztnev
    index = kereses(adatok,)

    #Ilyen nevű képviselőjelölt nem szerepel a nyilvántartásban!

def main():
    adatok = listaFeltoltes()
    #print(adatok)

    # 2. feladat
    print("A helyhatósági választáson",len(adatok),"képviselőjelölt indult.")

    # 3. feladat
    feladat3(adatok)

main()
