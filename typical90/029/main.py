W, N = map(int, input().split())
H = [0] * (W + 1)

for _ in range(N):
    L, R = map(int, input().split())
    maximum = max(H[L:R + 1])
    for i in range(L, R + 1):
        H[i] = maximum + 1
    print(maximum + 1)
