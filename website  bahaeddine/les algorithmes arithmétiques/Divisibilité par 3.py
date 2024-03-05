# Divisibilité par 3

def div3(n):
    ch = str(n)
    s = 0
    for i in range(len(ch)):
        s = s + int(ch[i])
    return s % 3 == 0


n = int(input("donner n"))
print(div3(n))
