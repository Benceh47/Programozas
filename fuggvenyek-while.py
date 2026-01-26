
#jancsi es juliska elmennek minden nap gombát gyüjteni, 14napig folyamatosan gyüjtik majd összevetik az adatokat.

def vaneKetjegyuListaban(szamok):

    i = 0
    while i < len(szamok) and not (szamok[i] >= 10 and szamok[i] <= 99):
        i += 1
    vane = i < len(szamok)
    return vane

def main():
    szamok = [2, 5, 6, 3, 7, 11, 9, 1, 2]
    print(szamok)
    # van-e kétjegyű szám a listában
    vaneKetjegyu = vaneKetjegyuListaban(szamok)
    print(vaneKetjegyu)

main()