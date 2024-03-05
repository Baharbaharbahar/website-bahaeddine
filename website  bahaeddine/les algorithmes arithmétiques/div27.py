def div27(n):
    while n > 999:
        s = 0
        while n != 0:
            s = s + n % 1000
            n = n // 1000
        n = s
    return n % 27 == 0


###### PP ######
n = int(input("Entrer un nombre positif:"))
if div27(n):
    print(n, "est divisivle par 27")
else:
    print(n, "n'est pas divisivle par 27")
