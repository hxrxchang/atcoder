A, B, X = map(int, input().split())

def price(n):
  return A * n + B * len(str(n))

ok = 0
ng = 10 ** 9 + 1

while not ng - ok == 1:
  mid = (ok + ng) // 2
  if price(mid) <= X:
    ok = mid
  else:
    ng = mid

print(ok)
