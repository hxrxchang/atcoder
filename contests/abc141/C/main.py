from collections import defaultdict

N, K, Q = map(int, input().split())
solved = defaultdict(int)

for _ in range(Q):
    A = int(input())
    solved[A] += 1

for i in range(1, N + 1):
    if K - Q + solved[i] > 0:
        print('Yes')
    else:
        print('No')
