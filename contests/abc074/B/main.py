N = int(input())
K = int(input())
X = list(map(int, input().split()))

cnt = 0
for x in X:
  cnt += min(x * 2, abs(K - x) * 2)

print(cnt)
