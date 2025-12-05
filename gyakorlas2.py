#0kérjen be egy szöveget és egy betüt!
#0.5nézze meg van-e az adott betű ha van
#1.adja meg hány darab betű van a szövegben!
szoveg=input("Adjon meg egy szöveget:")
betu=input("adjon meg egy betűt:")
db=0

for i in szoveg:
    if i==betu:
        db+=1
print("A szövegben",db, "darab",betu, " betű van.")

if db > 0:
    print("A szöveg tartalmazza a megadott betűt.")
else:
        print("a szövegben nincs ilyen betü.")

