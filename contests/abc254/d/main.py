# https://note.com/cell_tower_theta/n/nbb46326458da

N = int(input())
ans = 0
for i in range(1, N + 1):
    k = i
    p = 2
    while p * p <= k:
        while k % (p * p) == 0:
            k //= (p * p)
        p += 1
    p = 1
    while k * (p * p) <= N:
        ans += 1
        p += 1

print(ans)
