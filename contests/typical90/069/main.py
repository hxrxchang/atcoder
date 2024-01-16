N, K = map(int, input().split())
MOD = 10 ** 9 + 7

if N == 1:
  print(K)
  exit()
elif N == 2:
  print(K * (K - 1))
else:
  print(K * (K - 1) * pow(K - 2, N - 2, MOD) % MOD)
