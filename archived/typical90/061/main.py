Q = int(input())

from_top = []
from_bottom = []

for _ in range(Q):
  t, x = map(int, input().split())
  if t == 1:
    from_top.append(x)
  elif t == 2:
    from_bottom.append(x)
  else:
    if x <= len(from_top):
      print(from_top[-x])
    else:
      print(from_bottom[x - len(from_top) - 1])
