import math

N = int(input())

candidates = []

i = 1

while True:
    n = i ** 3
    if n > N:
        print(candidates[-1])
        break
    strn = str(n)
    if strn == strn[::-1]:
        candidates.append(n)
    i += 1

