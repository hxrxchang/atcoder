N = int(input())

# X[i]日経過後にX[j]人増減する
X = []
for i in range(N):
  A, B = map(int,input().split())
  X.append([A, 1])
  X.append([A + B, -1])

X.sort(key=lambda x: x[0])

ans = [0] * (N + 1)
# 人数
p_cnt = 0
for i in range(len(X) - 1):
  p_cnt += X[i][1]
  # 日数
  d_cnt = X[i + 1][0] - X[i][0]
  ans[p_cnt] += d_cnt

ans = ans[1:]
print(*ans)
