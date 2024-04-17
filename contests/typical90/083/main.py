import math

N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

boundary = math.sqrt(2 * N)
# 平方分割で、大きい頂点とその頂点の色をKey-Valueで持つ
big_nodes = {}
# 大きい頂点に隣接する小さい頂点を除外するためのグラフ
graph2 = [[] for _ in range(N)]

for i in range(N):
    if len(graph[i]) >= boundary:
        big_nodes[i] = 1
        update = []
        for node in graph[i]:
            if len(graph[node]) >= boundary:
                update.append(node)
        graph2[i] = update
    else:
        graph2[i] = graph[i]

Q = int(input())

# nodeが最後に更新されたクエリの番号を記録する
last_updated = [0] * N

# Qのi番目の色を記録する
yq = [0] * (Q + 1)
yq[0] = 1

for i in range(1, Q + 1):
    x, y = map(int, input().split())
    x -= 1

    if x in big_nodes:
        print(big_nodes[x])
        big_nodes[x] = y
        for node in graph2[x]:
            big_nodes[node] = y
    else:
        last = last_updated[x]
        for node in graph2[x]:
            last = max(last, last_updated[node])
            if node in big_nodes:
                big_nodes[node] = y
        print(yq[last])

    yq[i] = y
    last_updated[x] = i
