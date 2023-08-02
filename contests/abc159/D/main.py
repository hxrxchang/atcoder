from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

# 最初に各要素の個数を数えておく
cnt_dict = defaultdict(int)
for a in A:
  cnt_dict[a] += 1

# cnt[a][0] = aを2つ選ぶ組み合わせの数
# cnt[a][1] = aから要素数を1引いて、2つ選ぶ組み合わせの数
cnt = {}
total = 0
for a in cnt_dict.keys():
  first = cnt_dict[a] * (cnt_dict[a] - 1) // 2
  second = (cnt_dict[a] - 1) * (cnt_dict[a] - 2) // 2
  cnt[a] = (first, second)
  total += first

for n in range(N):
  ans = total - cnt[A[n]][0]
  ans += cnt[A[n]][1]
  print(ans)
