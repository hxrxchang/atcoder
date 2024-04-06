class UnionFind:
  def __init__(self, n):
    # parentsは要素が正の値のときはそのインデックスのルートを表す。
    # 負の値のときはそのインデックスはルートであり絶対値がそのルートが持つ要素数を表す。
    self.parents = [-1] * n

  def root(self, n):
    if self.parents[n] < 0:
      return n
    self.parents[n] = self.root(self.parents[n])
    return self.parents[n]

  def unit(self, a, b):
    a = self.root(a)
    b = self.root(b)
    if a == b:
      return
    # a, bはルートなので必ず負の値(そのルートがもつ要素数)になる
    if abs(self.parents[a]) < abs(self.parents[b]):
      b, a = a, b
    # ルートの要素数を更新
    self.parents[a] += self.parents[b]
    # サイズが小さい方のルートを大きい方のルートに繋げる
    self.parents[b] = a

  def is_same(self, a, b):
    return self.root(a) == self.root(b)

N, M = map(int, input().split())

uf = UnionFind(N)

x, y = 0, 0

for _ in range(M):
  A, B, C, D = list(input().split())
  A = int(A) - 1
  C = int(C) - 1
  # 親が一緒ということは、結べば閉路になるということ
  if uf.is_same(A, C):
    # そのノードが含まれるグラフにはじめて閉路ができるときにカウントしたいのでここでカウントする
    x += 1
  uf.unit(A, C)

for i in range(N):
  if uf.parents[i] < 0:
    y += 1

# uf内の全グラフ数から、閉路を含むグラフ数を引く
y = y - x

print(x, y)


