N = int(input())

if N % 2 == 1:
  print(0)
  exit()

cnt = 0
N //= 2
while N > 0:
  cnt += N // 5
  N //= 5

print(cnt)
