import string

H, W = map(int, input().split())
S = []
for _ in range(H):
  s = ''
  A = list(map(int, input().split()))
  for a in A:
    if a == 0:
      s += '.'
    else:
      st = string.ascii_uppercase[a - 1]
      s += st
  print(s)
