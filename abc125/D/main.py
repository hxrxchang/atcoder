N = int(input())
A = list(map(int, input().split()))
cnt = sum([i < 0 for i in A])

if cnt % 2 == 0:
  ans = sum([abs(i) for i in A])
  print(ans)
else:
  A2 = [abs(i) for i in A]
  target = A2[0]
  for a in A2:
    if a < target:
      target = a
  A2.remove(target)
  ans = sum(A2) - target
  print(ans)

