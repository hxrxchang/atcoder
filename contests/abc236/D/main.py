from itertools import combinations

N = int(input())
A = [list(map(int, input().split())) for i in range(N)]

combs = combinations(range(N * 2), 2)

ans = 0
for c in combs:
  print(c[0], c[1])
  # ans = max(ans, A[c[0]][c[1] - 1])

print(ans)

