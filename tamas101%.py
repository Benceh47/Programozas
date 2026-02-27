# a = 23
# b = "alma"
# c = True

# t = [a,b,c, ["k1","k2"]]
# t[0]
#irj egy függvényt ami megadja melyik honapan volt a legjobb eredmeny


def eredmeny(jegy, honapok):
    maxe = jegy[0]
    max_index = 0
    for i in range(1, len(jegy)):
        if jegy[i] > maxe:
            maxe = jegy[i]
            max_index = i
    return honapok[max_index]

def main(): 
    honapok = ["Január","február","március","április","május","junius","julius","augusztus","szeptember","oktober","november","december"]
    jani = [4.0, 3.8, 4.2, 4.1, 3.8, 4.2, 3.0, 3.6, 4.2, 4.1, 4.7, 4.2]
    print(eredmeny(jani, honapok))

main()