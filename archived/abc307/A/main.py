N = int(input())
A = list(map(int, input().split()))

res = [0] * N

for i, a in enumerate(A):
  res[i // 7] += a

print(*res)

