W, H, x, y = map(int, input().split())

a1 = W * H / 2
a2 = 0
if x == W / 2 and y == H / 2:
  a2 = 1

print(a1, a2)
