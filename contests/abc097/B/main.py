import math

X = int(input())

ans = 1
for i in range(2, int(math.sqrt(X)) + 1):
  k = 1
  while i ** k <= X:
    ans = max(ans, i ** k)
    k += 1

print(ans)
