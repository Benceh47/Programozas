import random
import math
a = random.randint(-5, 5) * 2
print("szám: " + str(a))

if a < 0:
    print("abs: " + str(a * -1))
    print("a szám negatív")
elif a > 0:
    print("abs: " + str(a))
    print("a szám pozitív")
else:
    print("abs: " + str(a))
    print("nulla")

if a >= 0:
    gyoka = math.sqrt(a)
    print("gyök: (" + str(a) + ") = " + str(gyoka))
else:
    print("Nincs gyök.")

# HF PDFből 8-13feladaat,
# felhasználótól bekérés
# szoveg = input("adjon meg egy számot:")


# szekvencia - utasitások sorozata
# szelekció- elágazás
# iteráció - ciklius, ismétlés

# HF megoldás

sec = 3923
ora = sec // 3600
perc = (sec - ora * 3600) // 60
masodperc = sec % 60
print(ora, "óra", perc, "perc", masodperc, "másodperc")
