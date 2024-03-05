def thueMorse(u0, n):
    for i in range(n):
        u = ""
        for j in range(len(u0)):
            if u0[j] == "1":
                u = u + "10"
            else:
                u = u + "01"
        u0 = u
        print(u)
    return u


######### PP ###########
u0 = input("entrer u0:")
n = int(input("Quel terme calcule?:"))
print("u" + str(n) + "=", thueMorse(u0, n))
