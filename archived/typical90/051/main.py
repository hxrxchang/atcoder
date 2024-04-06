from itertools import combinations
import bisect

N, K, P = map(int, input().split())
A = list(map(int, input().split()))

B, C = A[:N//2], A[N//2:]

# Bの中から0~K個選んだときのありえる合計金額を列挙
b_price = [[] for _ in range(K + 1)]
for i in range(K + 1):
  for c in combinations(B, i):
    b_price[i].append(sum(c))
  b_price[i].sort()

ans = 0
for i in range(K + 1):
  for c in combinations(C, i):
    idx = bisect.bisect_right(b_price[K - i], P - sum(c))
    ans += idx

print(ans)
