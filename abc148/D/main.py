N = int(input())
A = list(map(int, input().split()))

tmp = 1
cnt = 0
for a in A:
  if a != tmp:
    cnt += 1
  else:
    tmp += 1

if tmp == 1 and N > 1:
  print(-1)
else:
  print(cnt)
