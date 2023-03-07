N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

cnt = 0
for i in range(N):
  cnt += abs(A[i] - B[i])

print(cnt)
