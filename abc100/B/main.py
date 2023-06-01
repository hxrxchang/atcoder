D, N = map(int, input().split())

if D == 0:
  if N == 100:
    print(N + 1)
  else:
    print(N)
elif D == 1:
  if N == 100:
    print(N * 100 + 100)
  else:
    print(N * 100)
elif D == 2:
  if N == 100:
    print(N * 10000 + 10000)
  else:
    print(N * 10000)
