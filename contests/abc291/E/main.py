from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
into_num = [0] * N

for _ in range(M):
  x, y = map(int, input().split())
  graph[x - 1].append(y - 1)
  into_num[y - 1] += 1

numbers = [x + 1 for x in range(N)]
numbers.sort(reverse=True)

def topological_sort(G, into_num):
  #入ってくる有向辺を持たないノードを列挙
  q = deque()
  #V: 頂点数
  for i in range(N):
    if into_num[i]==0:
      q.append(i)
  #以下、幅優先探索
  ans = []
  while q:
    v = q.popleft()
    ans.append(v)
    for adj in G[v]:
      into_num[adj] -= 1 #入次数を減らす
      if into_num[adj]==0:
        q.append(adj) #入次数が0になったら、キューに入れる
  return ans

ans = topological_sort(graph, into_num)
print(ans)
