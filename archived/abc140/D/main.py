N, K = map(int, input().split())
S = list(input())

# 方針:
# 'L' と 'R' の変わり目を減らす
# 一度の操作で 'L' と 'R' の変わり目を最大2つ減らせる

# 'L' と 'R' の変わり目の数
a = 0
for i in range(N - 1):
  if S[i] != S[i + 1]:
    a += 1

ans = N - 1 - max(a - K * 2, 0)
print(ans)
