H, W = map(int, input().split())

board = [['W'] * W for _ in range(H)]

class UnionFind:
  def __init__(self, n):
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

def is_red(y, x, y2, x2):
  return board[y][x] == "R" and board[y2][x2] == "R"

def get_idx(y, x):
  return y * W + x

uf = UnionFind(H * W)

Q = int(input())
for _ in range(Q):
  query = list(map(int, input().split()))
  if query[0] == 1:
    y, x = query[1] - 1, query[2] - 1
    board[y][x] = "R"
    for item in [[y + 1, x], [y - 1, x], [y, x + 1], [y, x - 1]]:
      y2, x2 = item[0], item[1]
      if 0 <= y2 and y2 < H and 0<= x2 and x2 < W:
        if board[y2][x2] == "R":
          uf.unit(get_idx(y, x), get_idx(y2, x2))
  else:
    y, x, y2, x2 = query[1] - 1, query[2] - 1, query[3] - 1, query[4] - 1
    if is_red(y, x, y2, x2) and uf.is_same(get_idx(y, x), get_idx(y2, x2)):
      print("Yes")
    else:
      print("No")
