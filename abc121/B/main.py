N, M, C = map(int, input().split())
B = list(map(int, input().split()))
cnt = 0
for _ in range(N):
  A = list(map(int, input().split()))
  tmp = 0
  for m in range(M):
    tmp += A[m] * B[m]
  tmp += C
  if tmp > 0:
    cnt += 1

print(cnt)
