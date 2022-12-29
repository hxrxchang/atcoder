# Yesになる条件:
#   - グラフが閉路ではない
#   - 各Nodeが隣接する要素は2以下である。
class UnionFind:
  def __init__(self, n):
    # parentsは要素が正の値のときはそのインデックスのルートを表す。
    # 負の値のときはそのインデックスはルートであり絶対値がそのルートが持つ要素数を表す。
    self.parents = [-1] * n
    self.elements_cnt = [0] * n

  def root(self, n):
    if self.parents[n] < 0:
      return n
    self.parents[n] = self.root(self.parents[n])
    return self.parents[n]

  def unit(self, a, b):
    self.elements_cnt[a] += 1
    self.elements_cnt[b] += 1
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
for _ in range(M):
  A, B = map(int, input().split())
  A -= 1
  B -= 1
  if uf.is_same(A, B): #根が共通するということはuniteすると閉路を作ってしまう。
    print("No")
    exit()
  uf.unit(A, B)

if max(uf.elements_cnt) > 2:
  print("No")
else:
  print("Yes")

