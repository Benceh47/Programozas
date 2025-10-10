import math
import random


#szam= int(input("Adj meg egy számot: "))
#if szam % 2 == 0:
#    print("A szám páros")
#else:
#    print("A szám páratlan")

#kérjen be egy egy számot és mondja meg hogy 10-el osztható e?

szoveg= int(input("adjon meg egy számot: "))
if (szoveg % 10):
    print("nem osztható tízzel, utolsó számjegy:"+str(szoveg % 10))
else: 
     print("tizzel osztható ")

# kérjen be egy másik számot és irassa ki a két szám reciprokának az összegét
a= int(input("adjon meg egy számot: "))
if (szoveg != 0):
    if(a != 0):
        rec = 1/szoveg
        rec2 = 1/a 
        print(rec+rec2)
    else:
        print("a másodk számnak nincs reciproka")
else:
    print("az első számnak nincs reciproka")

# A két szám összegének gyökét mindig számoljuk ki, ha mindkettő megvan
if szoveg + a >= 0:
    gyokall = math.sqrt(szoveg + a)
    print("összeg gyöke: " + str(gyokall))
else:
    print("tamas hibaja hogy nemjó")

    #logikai opertorok
    #and, or, not, xor

    #HF bool algebra
    #HF kérjen be 3db számot lehet tört is, ez a három szám egy háromszőg három oldala.
    # 1. Derékszőgű?
    # 2 egyenlő szárú?
    # 3 szabályos-e a háromszög?