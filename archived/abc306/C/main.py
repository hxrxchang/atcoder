from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

data = defaultdict(list)

for i, a in enumerate(A):
  data[a].append(i)

data2 = []
for k in data.keys():
  data2.append([data[k][1], k])

data2.sort(key=lambda x: x[0])

ans = []
for d in data2:
  ans.append(d[1])

print(*ans)
