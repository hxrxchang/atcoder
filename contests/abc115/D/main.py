N, X = map(int, input().split())

def rec(N, X, L, S):
  if N == 0:
    return 1

  if X == 1:
    return 0
  elif X <= L[N - 1] + 1:
    return rec(N - 1, X - 1, L, S)
  elif X == L[N - 1] + 2:
    return S[N - 1] + 1
  elif X <= L[N - 1] * 2 + 2:
    return rec(N - 1, X - L[N - 1] - 2, L, S) + S[N - 1] + 1
  else:
    return S[N - 1] * 2 + 1

L = [1] * (N + 1)
S = [1] * (N + 1)

for i in range(1, N + 1):
  L[i] = L[i - 1] * 2 + 3
  S[i] = S[i - 1] * 2 + 1

ans = rec(N, X, L, S)

print(ans)
