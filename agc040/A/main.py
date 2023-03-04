S = input()
n = len(S) + 1

memo = [0] * n

for i in range(n - 1):
  s = S[i]
  if s == "<":
    memo[i + 1] = memo[i] + 1

print(memo)

for i in range(n - 2, -1, -1):
  s = S[i]
  if s == ">":
    print(memo[i], memo[i + 1])
    memo[i] = max(memo[i], memo[i + 1] + 1)

ans = sum(memo)

print(ans)
