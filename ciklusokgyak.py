#generáljon ki 10db egy jegyű , nem nullavéletlen számot 
# irassa ki a számok összegét  
import random

for a in range(1,11,1):
    velSzam=random.randint(1,9)
    osszeg += velSzam
    print(velSzam, end=" ")
print()
print("a számok összege:",osszeg)

#hány darab páros véletlen számot generált ki? melyik a legnagyobb véletlen szám?


