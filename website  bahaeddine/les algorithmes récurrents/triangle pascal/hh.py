import numpy as np


def remplir(n):
    global m
    x = 1
    for i in range((n / 2) - 1):
        ok = n - 1 - i
        for j in range(i, ok):
            m[i, j] = x
            x = x + 1
        for k in range(i + 1, ok):
            m[k, ok] = x
            x = x + 1
        for l in range(ok - 1, i - 1):
            m[ok, l] = x
            x = x + 1
        for e in range(ok - 1, i + 1 - 1):
            m[e, i] = x
            x = x + 1
