import math
import random


#szam= int(input("Adj meg egy számot: "))
#if szam % 2 == 0:
#    print("A szám páros")
#else:
#    print("A szám páratlan")

#kérjen be egy egy számot és mondja meg hogy 10-el osztható e?

#szoveg= int(input("adjon meg egy számot: "))
#if (szoveg % 10):
    #print("nem osztható tízzel, utolsó számjegy:"+str(szoveg % 10))
#else: 
     #print("tizzel osztható ")

# kérjen be egy másik számot és irassa ki a két szám reciprokának az összegét
#a= int(input("adjon meg egy számot: "))
#if (szoveg != 0):
    #if(a != 0):
        #rec = 1/szoveg
        #rec2 = 1/a 
        #print(rec+rec2)
    #else:
        #print("a másodk számnak nincs reciproka")
#else:
    #print("az első számnak nincs reciproka")

# A két szám összegének gyökét mindig számoljuk ki, ha mindkettő megvan
#if szoveg + a >= 0:
    #gyokall = math.sqrt(szoveg + a)
    #print("összeg gyöke: " + str(gyokall))
#else:
    #print("tamas hibaja hogy nemjó")

    #logikai opertorok
    #and, or, not, xor

    #HF bool algebra
    #HF kérjen be 3db számot lehet tört is, ez a három szám egy háromszőg három oldala.
    # 1. Derékszőgű?
    # 2 egyenlő szárú?
    # 3 szabályos-e a háromszög?

    #Generáljon ki három véletlen háromjegyű számot, amelyek 13al oszthatók
#állitsa ezeket orrendbe
#adja meg az átlagukat
#van e közöttük 4el végzödök?

# Összes háromjegyű, 13-mal osztható szám listába

#a = random.randint(100,1000) % 13
#b = random.randint(100,1000) % 13
#c = random.randint(100,1000) % 13

#szamok=[a, b, c]
#print(szamok)

a = random.randint(8,76)*13
b = random.randint(8,76)*13
c = random.randint(8,76)*13
szamjegy = int(input("adjon meg egy számjegyet "))
print(a, b, c)

if(a % 10 == szamjegy or b % 10 == szamjegy or c % 10 == szamjegy):
    print("Van "+str(szamjegy)+"-re végződő szám.")
else:
    print("Nincs "+str(szamjegy)+"-re végződő szám.")
