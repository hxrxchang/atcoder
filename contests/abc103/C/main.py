N = int(input())
A = list(map(int, input().split()))

cnt = 0
for i in range(N):
  cnt += A[i] - 1

print(cnt)
