N, K = map(int, input().split())
members = []
for _ in range(K):
  members.append(input())

members.sort()
for m in members:
  print(m)
