a = float(input("Adjon meg az első számot: "))
b = float(input("Adjon meg a második számot: "))
c = float(input("Adjon meg a harmadik számot: "))

# Háromszög szerkeszthetőségi feltétel
if a + b > c and a + c > b and b + c > a:
    print("A háromszög megszerkeszthető")
    # 1. Derékszögű-e?
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Derékszögű a háromszög")
    else:
        print("Nem derékszögű a háromszög")
    # 2. Egyenlő szárú-e?
    if (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
        print("Egyenlő szárú a háromszög")
    else:
        print("Nem egyenlő szárú a háromszög")
    # 3. Szabályos-e?
    if a == b and b == c:
        print("Szabályos háromszög")
    else:
        print("Nem szabályos háromszög")
else:
    print("A háromszög nem megszerkeszthető")

