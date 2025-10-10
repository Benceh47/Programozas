# változo deklarálása és inicializálása
# változo létrehozása és kezdőérték adása
# változoNev, "kezdoertek"
nev="Ribárik Bence"
osztaly= "10.b"
datum= "2025.09.08"
#"'"
#'"'
print(datum)
print(nev, osztaly, datum, sep="\n")

# operator 

#konkatenálás, concat. összefűzés - két szöveget!!!!!
összefűzés = nev+"bármit, akármit"+osztaly
print(összefűzés)

# többszörözés
soknev= nev 
print(soknev)

"""
-Szöveg -string - str
(-karakter)
-szám - egész lebegőpontos(tört)(float)
-logikai, true, false
"""

aEgesz = 123
bTort = 34.23
szSzam = "12"
logikai = True 

print("a Egész:", aEgesz)
print("b Tört:", bTort)
print("sz Szam:", szSzam)
print("logikai:", logikai)

# Egesz operatorok
print("a + 2 =",aEgesz + 2)
print("a - 2 =",aEgesz - 2)
print("a * 2 =",aEgesz * 2)
print("a / 2 =",aEgesz / 2)

#div egészrész, Mod - modulus(maradék)
# div - //
# mod - %

print("a div 8=", aEgesz//8)
print("a mod 8=", aEgesz % 9)

print(int(szSzam)+aEgesz)
print(str(aEgesz)+szSzam)

print(szSzam+str(aEgesz))
print(aEgesz+int(szSzam))
