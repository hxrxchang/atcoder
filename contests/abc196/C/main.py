N = int(input())

cnt = 0
for i in range(1, 1000000):
  n = int(str(i) * 2)
  if n <= N:
    cnt += 1
  else:
    break

print(cnt)
