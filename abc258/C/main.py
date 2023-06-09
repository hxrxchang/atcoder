N, Q = map(int, input().split())
S = list(input())

current = 0
for _ in range(Q):
  q, x = map(int, input().split())
  if q == 1:
    current = (current + x) % N
  if q == 2:
    print(S[x - current - 1])
