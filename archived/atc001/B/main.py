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
