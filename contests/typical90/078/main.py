N, M = map(int, input().split())

graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    # 無向グラフだが、自分より小さい頂点だけつなぐ
    if a > b:
        graph[a].append(b)
    else:
        graph[b].append(a)

cnt = 0
for g in graph:
    if len(g) == 1:
        cnt += 1

print(cnt)
