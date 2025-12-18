import random

n= 13 # lista elemszáma

lista =[]
for szamok in range(0,n,1):
    a = random.randint(0,20)
    lista.append(a)

print(lista)