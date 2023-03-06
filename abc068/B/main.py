N = int(input())

max = 0
max_cnt = 0

if N == 1:
  print(1)
  exit()

for i in range(1, N + 1):
  cnt = 0
  j = i
  while j >= 2:
    j = j / 2
    if j % 1 == 0:
      cnt += 1
    else:
      break
  if cnt > max_cnt:
    max_cnt = cnt
    max = i

print(max)
