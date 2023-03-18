N = int(input())
D, X = map(int, input().split())
total = X

for _ in range(N):
  A = int(input())
  cnt = 1
  i = 1
  while i * A + 1 <= D:
    cnt += 1
    i += 1
  total += cnt

print(total)


