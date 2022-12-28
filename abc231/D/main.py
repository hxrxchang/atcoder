# Yesになる条件:
#   - グラフが閉路ではない
#   - 各Nodeが隣接する要素は2以下である。
from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.elements_cnt = [0] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        self.elements_cnt[x] += 1
        self.elements_cnt[y] += 1
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

N, M = map(int, input().split())
uf = UnionFind(N)
for _ in range(M):
  A, B = map(int, input().split())
  A -= 1
  B -= 1
  if uf.find(A) == uf.find(B): #根が共通するということはuniteすると閉路を作ってしまう。
    print("No")
    exit()
  uf.union(A, B)

if max(uf.elements_cnt) > 2:
  print("No")
else:
  print("Yes")

