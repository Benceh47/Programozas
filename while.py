'''

elotesztelos ciklus azaz a while ciklus nem tudjuk hányszor fog lefutni/ismételni feltetelhez kotött akkor ismétel ha feltétel igaz

while(Feltetel):
    Utasitások(szekvencia)

'''

#generáljon véletlen számokat 0és 10 között amig nullast nem kapunk
import random 
#szam=random.randint(0,10)
#print(szam, end=" ")
#while(szam !=0):
#    szam=random.randint(0,10)
#    print(szam, end=" ")
#print()

    #kérjen be számokat addig amig a nullát nem adnak meg
#Velszam=int(input("adjon meg, egy számot:"))
#while(Velszam !=0):
 #       Velszam=int(input("adjon, meg egy számot:"))
#végén kiirja az átlagát

#atlag= input("adjon meg egy számot:")
#osszeg=0
#db=0
#while(atlag !="0"):
#    szam=int(atlag)
#    osszeg=osszeg+szam
#    db=db+1
#    atlag=input("adjon meg   még egy számot:")
#if db>0:
#    atlag=osszeg/db
#    print("a számok átlaga:", atlag)
#else:
#    print("nincs átlag")




    #aditt egy szöveg, adja meg hogy van-e benne x betű

szoveg= input("adjon meg egy szöveget:")
xbetu= 'x'
Xbetu= 'X"'
if xbetu or Xbetu in szoveg:
        print("van x betű a szövegben")
else:
            print("nincs xbbetű a szövegben")


        
