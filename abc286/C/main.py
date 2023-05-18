import math

N, A, B = map(int, input().split())
S = input()

ans = float('inf')
for i in range(N):
  S_ = S[i:] + S[:i]
  tmp = i * A
  for j in range(math.ceil(N / 2)):
    if S_[j] != S_[-1-j]:
      tmp += B
  ans = min(ans, tmp)

print(ans)
