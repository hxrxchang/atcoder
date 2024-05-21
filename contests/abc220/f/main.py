import sys
sys.setrecursionlimit(10**6)

def dfs1(node, parent):
    subtree_size[node] = 1
    dp[node] = 0
    for neighbor in tree[node]:
        if neighbor != parent:
            dfs1(neighbor, node)
            subtree_size[node] += subtree_size[neighbor]
            dp[node] += dp[neighbor] + subtree_size[neighbor]

def dfs2(node, parent):
    for neighbor in tree[node]:
        if neighbor != parent:
            dp[neighbor] = dp[node] - subtree_size[neighbor] + (N - subtree_size[neighbor])
            dfs2(neighbor, node)

def solve(N, edges):
    global tree, dp, subtree_size
    tree = [[] for _ in range(N + 1)]
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    # 初期化
    dp = [0] * (N + 1)
    subtree_size = [0] * (N + 1)

    # 一次DP
    dfs1(1, -1)

    # 全方位DP
    dfs2(1, -1)

    return dp[1:]

# 入力例
N = int(input())
edges = [list(map(int, input().split())) for _ in range(N - 1)]

# 実行
result = solve(N, edges)

for r in result:
    print(r)
