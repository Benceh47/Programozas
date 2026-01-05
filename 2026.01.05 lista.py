#generáljon egy listába 13db olyan négyjegyű véletlen számokat amik 3,5,7 re végződnek
#hány darab 3-ra 5-re és 7-re végződő szám van
import random

n = 13

lista_c=[]
for szamok in range(0,n,1):
    a = random.randint(100,999) 
    szam= a*10 + random.choice([3,5,7])

    lista_c.append(szam)
print(lista_c)

#végződés
db_3=0
db_5=0
db_7=0
for szam in lista_c:
    utolso_szamjegy= szam %10
    if utolso_szamjegy ==3:
        db_3+=1
    elif utolso_szamjegy ==5:
        db_5+=1
    else:
        db_7+=1
print("3-ra végződő számok:",db_3)
print("5-re végződő számok:",db_5)
print("7-re végződő számok:",db_7)

#számtani átlag
# hány darab szám van átlag alatt
#mértani átlag
#a mértani átlag alatti számok összege
#30db szám, 13 és 17-re végződő számokkal hány osztható 13-mal és 17-tel
#bekérsz egy hosszaabb szöveget, hány darab felhasználó által megadott betű van benne
# bekérsz két szót mond meg adott, indexen hány darab betű eltérés vanpl.(alma, alkat -> 2 eltérés)
