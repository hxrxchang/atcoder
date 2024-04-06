X, Y = map(int, input().split())

cnt = 0
tmp = X
while tmp <= Y:
  cnt += 1
  tmp *= 2

print(cnt)
