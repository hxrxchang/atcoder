N, M, X = map(int, input().split())
A = list(map(int, input().split()))

bloks = [0] * (N + 1)
for a in A:
  bloks[a] = 1

first = sum(bloks[:X+1])
second = sum(bloks[X:])

print(min(first, second))
