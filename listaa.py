
import random
szamok = []
while len(szamok) < 13:
    szam = random.randint(-950, 950)
    if szam % 100 == 50 or szam % 100 == 0:
        szamok.append(szam)

print(szamok)


db = 0
for szam in szamok:
    if szam < 0 and szam % 100 == 0:
        db += 1
print("dupla nullára végződő negativ számok:", db)