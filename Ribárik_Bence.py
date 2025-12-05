#1 feladat

import random
import math
#a

a=random.randint(10,99)
print(a)

#b
for szamok in range(0, a, 1):
    b = random.randint(100,999)
    print (b, end=" ") 

    db = 0
if b % 3 == 0:
        db += 1
print()
print("3mal oszható számok összege:", db)


  

           




#2feladat
szoveg=input("adjon meg egy szöveget:")
print(szoveg)
