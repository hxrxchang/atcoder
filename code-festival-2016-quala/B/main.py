N = int(input())
A = list(map(int, input().split()))

memo = {}
cnt = 0
for i, a in enumerate(A):
    i += 1
    pair = tuple(sorted([i, a]))
    if pair in memo:
        cnt += 1
    else:
        memo[pair] = 1

print(cnt)
