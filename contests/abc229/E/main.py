class UnionFind:
  def __init__(self, n):
    # parentsは要素が正の値のときはそのインデックスのルートを表す。
    # 負の値のときはそのインデックスはルートであり絶対値がそのルートが持つ要素数を表す。
    self.parents = [-1] * n
    # グループの数
    self.__group_cnt = n

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
    # 連結されるごとにグループの数を減らす
    self.__group_cnt -= 1

  def is_same(self, a, b):
    return self.root(a) == self.root(b)

  def group_cnt(self):
    return self.__group_cnt

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
  A, B = map(int, input().split())
  A -= 1
  B -= 1
  graph[A].append(B)

ans = [0] * N
uf = UnionFind(N)
for u in reversed(range(N)):
  ans[u] = uf.group_cnt() - (u + 1)
  for v in graph[u]:
    uf.unit(u, v)

for a in ans:
  print(a)
