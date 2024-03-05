def PPCM(x, y):
    i = 1
    r = x * i
    while x % y != 0:
        r = x * i
        i = i + 1
    return r


x = int(input("donner x"))
y = int(input("donner y"))
print(PPCM(x, y))
print(PPCM(r))
