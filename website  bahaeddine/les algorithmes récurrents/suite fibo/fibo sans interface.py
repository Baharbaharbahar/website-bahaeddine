

def fibo(n):
    u0=1
    u1=1
    for i in range(2,n+1):
        u=u1+u0
        u0=u1
        u1=u
    return u




######### PP ##########
n=int(input("Quel terme calculer?:"))
print("U"+str(n)+"=",fibo(n))
