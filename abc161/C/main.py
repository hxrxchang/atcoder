N, K = map(int, input().split())

if N % K == 0:
  print(0)
  exit()

N = N % K

min = N
while True:
  N = abs(N - K)
  if N < min:
    min = N
  else:
    print(min)
    break

