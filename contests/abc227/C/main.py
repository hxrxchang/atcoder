from math import log2

N = int(input())

X = N
Y = N // 2
Z = Y // 2

cnt = 0
print(log2(X), log2(Y), log2(Z))
for i in range(1, int(log2(X)) + 1):
    for j in range(1, int(log2(Y) + 1)):
        for k in range(1, int(log2(Z) + 1)):
            if (X // i) * (Y // j) * (Z // k) <= N:
                cnt += 1

print(cnt)
