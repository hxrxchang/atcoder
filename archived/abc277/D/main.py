N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

# 同じ数字、連続する数字をグループ化
G = [[A[0]]]
for i in range(1, N):
  if G[-1][-1] == A[i] or G[-1][-1] + 1 == A[i]:
    G[-1].append(A[i])
  else:
    G.append([A[i]])

# (X + 1) % Mのカードも捨てられるので、Aの最大値 + 1がMの場合、0を含むグループを一緒にできる
if len(G) >= 2 and G[0][0] == 0 and G[-1][-1] + 1 == M:
  g = G[0] + G[-1]
  G.pop(0)
  G.pop(-1)
  G.append(g)

sum_a = sum(A)
ans = float('inf')

for g in G:
  ans = min(ans, sum_a - sum(g))

print(ans)
