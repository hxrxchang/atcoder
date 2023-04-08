N, Q = map(int, input().split())

following = set()

for _ in range(Q):
  T, A, B = map(int, input().split())
  if T == 1:
    following.add((A, B))
  elif T == 2:
    following.discard((A, B))
  elif T == 3:
    if (A, B) in following and (B, A) in following:
      print("Yes")
    else:
      print("No")


