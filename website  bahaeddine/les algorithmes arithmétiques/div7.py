def div7(n):
    while n > 99:
        n = (n // 10) - 2 * (n % 10)
    return n % 7 == 0


###### PP ######
n = int(input("Entrer un nombre positif:"))
if div7(n):
    print(n, "est divisivle par 7")
else:
    print(n, "n'est pas divisivle par 7")
