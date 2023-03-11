N = int(input())
A = list(map(int, input().split()))

called = [False] * (N)

for i, a in enumerate(A):
  if not called[i]:
    called[a - 1] = True

K = called.count(False)
ans = []
for i, a in enumerate(called):
  if not a:
    ans += [i + 1]

print(K)
print(*ans)
