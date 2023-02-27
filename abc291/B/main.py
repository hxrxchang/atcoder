N = int(input())
X = list(map(int, input().split()))
X.sort()
X = X[N: -N]

ans = sum(X) / len(X)

print(ans)
