from collections import defaultdict

N = int(input())

cnt = defaultdict(int)
for _ in range(N):
    A, C = map(int, input().split())
    if cnt[C] == 0:
        cnt[C] = A
    else:
        cnt[C] = min(cnt[C], A)


print(max(cnt.values()))
