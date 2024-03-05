def thueMorse(u0,n):
    for i in range(n):
        u=""
        for j in range(len(u0)):
            if u0[j]=="1":
                u=u+"10"
            else:
                u=u+"01"
        u0=u
        #print(u)
    return u




########### PP ################
uo=input("entrer U0:")
n=int(input("Quel terme calcule?:"))
print("U"+str(n)+"=",thueMorse(uo,n))