# Divisibilité par 5
def div5(n):
    return n % 10 in [0, 5]


n = int(input("donner n :"))

print(div5(n))
