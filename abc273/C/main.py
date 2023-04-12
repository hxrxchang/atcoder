N = int(input())
A = list(map(int, input().split()))

A.sort()
memo = {}
for a in A:
    if a in memo:
        memo[a] += 1
    else:
        memo[a] = 1


