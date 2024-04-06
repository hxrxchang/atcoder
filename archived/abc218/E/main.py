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
edges = [list(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x:x[2])

# 全部辺を削除して、報酬をすべて受け取った前提でスタート
# 連結を維持したいので、わざわざ罰金を払って辺を削除する必要はないため、マイナスの報酬は無視
reward = 0
for edge in edges:
  if edge[2] > 0:
    reward += edge[2]

uf = UnionFind(N)
for edge in edges:
  # 罰金を払って辺を削除することはないので、マイナスの場合は無条件で連結
  if edge[2] <= 0:
    uf.unit(edge[0]-1, edge[1]-1)
  else:
    if not uf.is_same(edge[0]-1, edge[1]-1):
      reward -= edge[2]
      uf.unit(edge[0]-1, edge[1]-1)

print(reward)
