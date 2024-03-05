def thueMorse(u0,n):
    u=uo
    for i in range(n):
        j=0
        #print(u)
        while j<len(u):
            if u[j]=="1":
                u=u[0:j+1]+"0"+u[j+1:len(u)]
            else:
                u=u[0:j+1]+"1"+u[j+1:len(u)]
            j=j+2           
    return u




########### PP ################
uo=input("entrer U0:")
n=int(input("Quel terme calcule?:"))
print("U"+str(n)+"=",thueMorse(uo,n))