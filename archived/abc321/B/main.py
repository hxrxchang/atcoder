import copy

N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(100 + 1):
  B = copy.deepcopy(A)
  B.append(i)
  B.sort()
  B = B[1:N-1]
  if sum(B) >= X:
    print(i)
    exit()

print(-1)
