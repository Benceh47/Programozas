#hf
#töls fel egy 13elemű listát [0,20] közötti véletlen számmal
#számok átlaga 
#Hány darab párosz szám van a listában.
#van-e benne nula



"""
lista- dinamikus
tudunk bele uj elemet rakni ezzel no az elemszam
tudunk belöle törölni ezáltal csökken az elemszam
lekérhető bármelyik eleme
módositható bármelyik elem
deklarálás:
lista_neve=[]
uj elem hozzáadása:
lista_neve.append(ujelem)
elem törlése:
lista_neve.remove(elem)
beégett lista:
lista_neve= [3,2,5,7,1]
lista hossza:
len(lista_neve)
"""
szamok=[3,2,5,7,1]
print(szamok)
szamok.append(12)
print(szamok)
szamok.remove(3)
print(szamok)
print("első elem:", szamok[0])
print("Utólso elem:", szamok[len(szamok)-1])
print("Lista, hosszúsága:", len(szamok))







#szövegben van e sz betű
szoveg="geza kek az eg"
dube ="ny" #dupla betű
print(szoveg)
print("ezt keressük:",dube)
#if "sz" in szoveg:
#    print("van sz betű a szövegben")
#else:
#    print("nincs sz betű a szövegben")
index=0
while(index < len(szoveg)-1 and not (szoveg[index] == dube[0] and szoveg[index+1] == dube[1] )):
    index+=1
if(index<len(szoveg) -1):
    print("van benne", dube)
else:
    print("nincs benne", dube)

#palindrom-e
ujszoveg = ""
for index in range(len(szoveg)-1,-1,-1):
    ujszoveg += szoveg[index]
if (ujszoveg == szoveg):
    print("a szöveg palindrom.")
else:
    print("a szöveg nem palindrom.")

j=0
while(j<len(szoveg)/2 and szoveg[j] == szoveg[len(szoveg)-1-j]):
    j+=1
if(j<len(szoveg)/2):
    print("A szöveg palindrom.")
else:
    print("a szöveg nem palindrom.")

