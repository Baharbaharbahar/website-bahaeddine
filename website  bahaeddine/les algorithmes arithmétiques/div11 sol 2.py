def div11(n):
    s = 0
    for i in range(len(str(n))):
        s = s + (-1)**i * int(str(n)[i])
    return s % 11 == 0


# Exemple: n=72446
# (2+4)-(7+4+6)
# peut être écrite -7+2-4+4-6
# on voit bien qu'il suffit d'alterner le signe
# on peut exploiter la propriété mathématique
# (-1) puissance n (=1 si n est pair et =-1 sinon)
####### PP #########
n = int(input("Entrer un nombre positif:"))
if div11(n):
    print(n, "est divisivle par 11")
else:
    print(n, "n'est pas divisivle par 11")
