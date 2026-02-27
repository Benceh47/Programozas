def listaFeltoltes():
    lista = []
    db = int(input())
    for i in range(db):
        st = input().split(' ')
        lista.append((int(st[0]), int(st[1]), st[2], st[3],st[4]))
    return lista

def kereses(lista, vn, kn):
    i = 0
    while(i<len(lista) and not(lista[i][2]== vn and lista[i][3]== kn)):
        i+=1
    if(i<len(lista)):
        return i
    else:
        return -1


def feladat3(adatok):
    vezeteknev = input("Adja meg a vezetéknevet: ")
    keresztnev = input("Adja meg a keresztnevet: ")
    #nev = input("Adjam egy teljes nevét szóközzel elválasztva: ").split(" ")
    # nev[0] - vezeteknev, nev[1] - keresztnev
    index = kereses(adatok,vezeteknev, keresztnev)
    if(index >= 0):
        print(adatok[index][1])
    else:
        print(" Ilyen nevű képviselőjelölt nem szerepel a nyilvántartásban! ")

    #Ilyen nevű képviselőjelölt nem szerepel a nyilvántartásban!


def osszesSzavazat(adatok):
    osszeg = 0
    for i in range(len(adatok)):
        osszeg += adatok[i][1]
    return osszeg


def feladat4(adatok):
    szavazatokSzama = osszesSzavazat(adatok)
    mindenki = 12345  # Ez a jogosultak száma, ahogy meg van adva



def main():
    adatok = listaFeltoltes()
    #print(adatok)

    # 2. feladat
    print("A helyhatósági választáson",len(adatok),"képviselőjelölt indult.")

    # 3. feladat
    feladat3(adatok)

    #4. feladat
    feladat4(adatok)
main()


# #4. Határozza meg, hányan adták le szavazatukat, és mennyi volt a részvételi arány! 
# (A részvételi arány azt adja meg, hogy a jogosultak hány százaléka vett részt 
# a szavazáson.) A részvételi arányt két tizedesjegy pontossággal, százalékos formában írja 
# ki a képernyőre! 
# Például: 
# A választáson 5001 állampolgár, a jogosultak 40,51%-a vett részt. 
# gyakorlati vizsga 1211 11 / 12 2013. május 13. 
# Informatika — emelt szint Azonosító 
# jel: 
 
# 5. Határozza meg és írassa ki a képernyőre az egyes pártokra leadott szavazatok arányát 
# az összes leadott szavazathoz képest két tizedesjegy pontossággal! A független jelölteket 
# együtt, „Független jelöltek” néven szerepeltesse! 
# Például: 
# Zöldségevők Pártja= 12,34% 
# Független jelöltek= 23,40% 
# 6. Melyik jelölt kapta a legtöbb szavazatot? Jelenítse meg a képernyőn a képviselő vezetékés utónevét, valamint az őt támogató párt rövidítését, vagy azt, hogy független! Ha több 
# ilyen képviselő is van, akkor mindegyik adatai jelenjenek meg! 