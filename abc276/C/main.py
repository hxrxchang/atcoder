# 解説 https://qiita.com/MoroeTachibana-oh/items/7083f8bd2634d70846da#1-4-c%E5%95%8F%E9%A1%8C-previous-permutation
N = int(input())
P = list(map(int, input().split()))

# P[j]より右は単調増加
j = N - 2
while P[j] < P[j + 1]:
  j -= 1

# P[k] は P[j]より右でP[j]未満の最大値
k = N - 1
while P[j] < P[k]:
  k -= 1

# 入れ替え
P[j], P[k] = P[k], P[j]
ans = P[:j+1]
# 単調減少になるようにsort
ans += P[j + 1:][::-1]

print(*ans)
