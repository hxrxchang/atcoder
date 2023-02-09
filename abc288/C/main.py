class UnionFind:
  def __init__(self, n):
    self.parents = {}

  def root(self, item):
    if self.parents.get(item) == None:
      self.parents[item] = item
      return item
    if self.parents.get(item) == item:
      return item
    self.parents[item] = self.root(self.parents.get(item))
    return self.parents[item]

  def unit(self, a, b):
    a = self.root(a)
    b = self.root(b)
    if a == b:
      return
    self.parents[a] = b

  def is_same(self, a, b):
    return self.root(a) == self.root(b)

N, M = map(int, input().split())

uf = UnionFind(N)

cnt = 0
for _ in range(M):
  A, B = map(int, input().split())
  if uf.is_same(A, B):
    cnt += 1
  uf.unit(A, B)

print(cnt)
