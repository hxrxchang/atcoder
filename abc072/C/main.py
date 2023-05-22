from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

cnt = defaultdict(int)
for a in A:
  cnt[a] += 1

set_A = set(A)

ans = 0
for a in set_A:
  ans = max(ans, cnt[a - 1] + cnt[a] + cnt[a + 1])

print(ans)
