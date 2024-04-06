A, B, C = map(int, input().split())

if A + B + 1 >= C:
  ans = B + C
  print(ans)
else:
  ans = B + A + B + 1
  print(ans)
