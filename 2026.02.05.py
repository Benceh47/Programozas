import random

def ListaFeltoltes():

    lista = []
    for i in range(0,17,1):
        valsz = random.randint(0,100)
        if(valsz >=50):
            lista.append(random.randint(120,200))
        else:
            lista.append(random.randint(50,120))
    return lista

def ListaAtlag(lista):
    atlag = 0
    for i in range(0,len(lista),1):
        atlag += lista[i]
    return atlag

def ListaMaximum(lista):
    maxe = lista[0]
    for i in range(1,len(lista),1):
        if(lista[i]>maxe):
            maxe = lista[i]
    return maxe

def ListaMinimum(lista):
    mine = lista[0]
    for i in range(1,len(lista),1):
        if(lista[i]<mine):
            mine = lista[i]
    return mine

def ListaTerjedelme(lista):
    maximum = ListaMaximum(lista)
    minimum = ListaMinimum(lista)
    return maximum - minimum

def main():

    pontok= ListaFeltoltes()
    print(pontok)

#2 feladat
    atlag = ListaAtlag(pontok)
    print("Átlag:", round(atlag,2))

# 3. feladat
    terjedelem = ListaTerjedelme(pontok)
    print("Terjedelem:",terjedelem)
main()