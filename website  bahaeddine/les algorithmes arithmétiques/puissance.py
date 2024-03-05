# fonction iteratif puissance
def puis(x, y):
    p = 1
    for i in range(1, x + 1):
        p = p * x
    return p


x = int(input("donner svp x :"))
y = int(input("donner svp y:"))
print(puis(x, y))
# fonction recursif puissance


def puis(x, y):
    if y == 0:
        return 1
    else:
        return y * puis(x, y - 1)


x = int(input("donner x :"))
y = int(input("donner y:"))
print(puis(x, y))
