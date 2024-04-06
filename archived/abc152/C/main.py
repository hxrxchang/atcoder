N = int(input())
P = list(map(int, input().split()))

minimum_p = P[0]
cnt = 0
for p in P:
    if p <= minimum_p:
        cnt += 1
        minimum_p = p

print(cnt)
