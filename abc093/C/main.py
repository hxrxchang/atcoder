numbers = list(map(int, input().split()))

cnt = 0
while True:
  numbers.sort()
  A, B, C = numbers[0], numbers[1], numbers[2]
  if C - A == 1 and C - B == 1:
    cnt += 1
    break
  elif C - A == 2 and B == C:
    cnt += 1
    break
  else:
    numbers[0] += 2
    cnt += 1

print(cnt)
