def premier(x):
    nb = 0
    for i in range(1, x + 1):
        if x % i == 0:
            nb = nb + 1
    return nb == 2


x = int(input("donner x:"))
print(premier(x))
