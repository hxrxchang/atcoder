N, L, R = map(int, input().split())
A = list(map(int, input().split()))

ans = []
for a in A:
    if a < L or L <= a < R:
        ans.append(L)
    else:
        ans.append(R)

print(*ans)
