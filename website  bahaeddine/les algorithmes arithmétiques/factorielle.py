# fonction iteratif factorielle

def fact(x):
    f = 1
    for i in range(2, x + 1):
        f = f * i
    return f


x = int(input("donner x;"))
print(fact(x))
# fonction recursif factorielle


def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x - 1)


x = int(input("donner x:"))
print(fact(x))
