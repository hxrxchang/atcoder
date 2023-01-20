N = int(input())

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

uf = UnionFind(N)

for _ in range(N):
  first, second = input().split()
  print(uf.parents)
  # 新たにa,bに辺を張るとき，すでにa,bが同じグループに属していれば，この操作で閉路ができる．
  if uf.is_same(first, second):
    print("No")
    exit()
  uf.unit(first, second)

print("Yes")

