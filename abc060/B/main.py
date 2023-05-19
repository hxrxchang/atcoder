A, B, C = map(int, input().split())

i = 1
while True:
  if (A * i) % B == C:
    print('YES')
    exit()
  elif (A * i) % B == 0:
    print('NO')
    exit()
  i += 1
