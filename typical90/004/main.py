H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

rows = []
for i in range(H):
  v = 0
  for j in range(W):
    v += A[i][j]
  rows.append(v)

columns = []
for i in range(W):
  v = 0
  for j in range(H):
    v += A[j][i]
  columns.append(v)

for i in range(H):
  ans = []
  for j in range(W):
    item = A[i][j]
    val = rows[i] + columns[j]
    # 縦と横両方に自分が含まれるから自分1つ分引く
    val -= item
    ans.append(val)
  print(*ans)


