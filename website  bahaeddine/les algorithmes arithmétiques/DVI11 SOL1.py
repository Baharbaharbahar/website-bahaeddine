def div11(n):
    return (somIndImp(n) - somIndPair(n)) % 11 == 0


def somIndImp(n):
    chn = str(n)
    s = 0
    for i in range(len(chn)):
        if i % 2 != 0:
            s = s + int(chn[i])
    return s


def somIndPair(n):
    chn = str(n)
    s = 0
    for i in range(len(chn)):
        if i % 2 == 0:
            s = s + int(chn[i])
    return s


####### PP #########
n = int(input("Entrer un nombre positif:"))
if div11(n):
    print(n, "est divisivle par 11")
else:
    print(n, "n'est pas divisivle par 11")
