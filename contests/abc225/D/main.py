N, Q = map(int, input().split())

front = [None for _ in range(N + 1)]
back = [None for _ in range(N + 1)]

for _ in range(Q):
  inp = list(map(int, input().split()))
  if inp[0] == 1:
    back[inp[1]] = inp[2]
    front[inp[2]] = inp[1]
  elif inp[0] == 2:
    back[inp[1]] = None
    front[inp[2]] = None
  else:
    target = inp[1]
    ans = []

    # frontを後ろから見ていく
    while target is not None:
      ans.append(target)
      target = front[target]
    ans.reverse()

    # backを前から見ていく
    target = back[inp[1]]
    while target is not None:
      ans.append(target)
      target = back[target]

    print(len(ans), *ans)
