N = int(input())
N += 1

ans = 0

while N > 0:
  if N < 10:
    ans += N - 1
  else:
    ans += 9
  N //= 10

print(ans)
