
import random
szamok = []
while len(szamok) < 13:
    szam = random.randint(-950, 950)
    if szam % 100 == 50 or szam % 100 == 0:
        szamok.append(szam)

print(szamok)


# db = 0
# for szam in szamok:
#     if szam < 0 and szam % 100 == 0:
#         db += 1
# print("dupla nullára végződő negativ számok:", db)


# #irjon egy fv-t ami bármilyen lista elemeire kiszámolja az átlagát




# def listaAtlaga(szamok):
#     osszeg = 0
#     for elem in szamok:
#         osszeg+=elem
#     atlag = osszeg/len(szamok)
#     return atlag

# def pozitivSzamokAtlaga(szamok):
#     db=0
#     osszeg = 0
#     for elem in szamok: # végigmegyünk a lista összes elemén
#         if(elem>0):
#             db+=1
#             osszeg +=elem
#     atlag = osszeg /db
#     return atlag


def maximumIndex(szamok):
    maxi=0
    for i in range(1,len(szamok),1):
        if(szamok[i]>szamok[maxi]):
            maxi=i
    return maxi

def minimumIndex(szamok):
    mini= 0
    for i in range(1,len(szamok),1):
        if(szamok[i]<szamok[mini]):
            mini= i
    return mini


def terjedelem(szamok):
    maxe = maximumIndex(szamok)
    mine = minimumIndex(szamok)
    return maxe - mine
# listaAtlaga= listaAtlaga(szamok)
# print("az elsö lista, átlaga:",listaAtlaga)

# print("az első lista pozitiv számainak átlaga:",pozitivSzamokAtlaga(szamok))
maxIndexszamok = maximumIndex(szamok)

print("első legnagyobb elem helye:", maxIndexszamok+1)

minIndexszamok= minimumIndex(szamok)
# print("lista terjedelme:",max(szamok)-min(szamok))
print("lista maximum",maximumIndex(szamok))
print("lista minimum",minimumIndex(szamok))
print("lista terjedelem", terjedelem(szamok))


#irjon fv-t ami vissza adja a listánk terjedelmét, terjedelem = Maxmimum - minimum
