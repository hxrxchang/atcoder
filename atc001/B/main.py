N, Q = map(int, input().split())

class UnionFind:
  def __init__(self, n):
    self.n = n
    self.parents = list(range(n))
    self.size = [1] * n

  # 要素iのルートを返す
  def find(self, i):
    while self.parents[i] != i:
      self.parents[i] = self.parents[self.parents[i]]
      i = self.parents[i]
    return i

  # iを含む木とjを含む木を結合する
  def union(self, i, j):
    if self.find(i) == self.find(j):
      return
    elif self.size[self.find(i)] < self.size[self.find(j)]:
      self.size[self.find(j)] = self.size[self.find(i)] + self.size[self.find(j)]
      self.parents[self.find(i)] = self.find(j)
    else:
      self.size[self.find(i)] = self.size[self.find(j)] + self.size[self.find(i)]
      self.parents[self.find(j)] = self.find(i)

  def is_same(self, i, j):
    if self.find(i) == self.find(j):
      return True
    else:
      return False

  def get_size(self, i):
    return self.size[self.find(i)]

uf = UnionFind(N)
for _ in range(Q):
  P, A, B = map(int, input().split())
  if P == 0:
    uf.union(A, B)
  else:
    if uf.is_same(A, B):
      print("Yes")
    else:
      print("No")
