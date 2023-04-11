N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

diff = 0
for i in range(N):
  diff += abs(A[i] - B[i])

move_cnt = K - diff

if move_cnt >= 0 and move_cnt % 2 == 0:
  print("Yes")
else:
  print("No")
