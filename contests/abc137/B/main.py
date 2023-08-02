K, X = map(int, input().split())

A, B = X - K + 1, X + K

ans = list(range(A, B))

print(*ans)
