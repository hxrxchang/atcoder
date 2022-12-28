class UnionFind:
  def __init__(self, n):
    self.parents = list(range(n))

  def root(self, i):
    if self.parents[i] == i:
      return i
    self.parents[i] = self.root(self.parents[i])
    return self.parents[i]

  def unit(self, i, j):
    i = self.root(i)
    j = self.root(j)
    if i == j:
      return
    else:
      self.parents[i] = j

  def is_same(self, i, j):
    return self.root(i) == self.root(j)

N, Q = map(int, map(int, input().split()))
uf = UnionFind(N)
for _ in range(Q):
  P, A, B = map(int, input().split())
  if P == 0:
    uf.unit(A, B)
  elif P == 1:
    if uf.is_same(A, B):
      print("Yes")
    else:
      print("No")
