def main():
    szoveg2 = "2026.02.19 3 Programozás"
    #2 - február
    tordelt2 = szoveg2.split(" ")
    datum = tordelt2[0].split(".")
    honap_szam = int(datum[1])
    honapok = ["január", "február", "március", "április", "május", "június", "július", "augusztus", "szeptember", "október", "november", "december"]
    print(honapok[honap_szam-1])

    szoveg3 = "ABC-123, Kis Pista, KJ358638351, 1992.03.10"
    # év?
    # vezetéknév?
    tordelt3 = szoveg3.split(", ")
    # év
    datum3 = tordelt3[3].split(".")
    ev = datum3[0]
    print("Év:", ev)
    # vezetéknév
    nev = tordelt3[1].split(" ")
    vezeteknev = nev[0]
    print("Vezetéknév:", vezeteknev)

main()