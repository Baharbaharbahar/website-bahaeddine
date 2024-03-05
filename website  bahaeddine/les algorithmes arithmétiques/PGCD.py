# fonction iteratif PGCD
def PGCD(x, y):
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x


x = int(input("donner x"))
y = int(input("donner y"))
print(PGCD(x, y))
# fonction recursif puissance


def PGCD(x, y):
    if x == y:
        return x
    elif x > y:
        return PGCD(x - y, y)
    else:
        return PGCD(x, y - x)


x = int(input("donner x"))
y = int(input("donner y"))
print(PGCD(x, y))
