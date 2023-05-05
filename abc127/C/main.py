N, M = map(int, input().split())

max_l = 0
min_r = 10 ** 5

for _ in range(M):
    L, R = map(int, input().split())
    if L > max_l:
        max_l = L
    if R < min_r:
        min_r = R

print(max(0, min_r - max_l + 1))
