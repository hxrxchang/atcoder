N = int(input())
S = list(map(int, input().split()))

A = []
for i in range(N):
  if i == 0:
    A.append(S[0])
  else:
    cnt = 0
    for j in range(i):
      cnt += A[j]
    a = S[i] - cnt
    A.append(a)

print(*A)
