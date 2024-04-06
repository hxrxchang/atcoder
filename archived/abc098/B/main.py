N = int(input())
S = input()

ans = 0

for i in range(1, N - 1):
  pre = list(set(S[:i]))
  suf = list(set(S[i:]))
  tmp = 0
  for p in pre:
    if p in suf:
      tmp += 1
  ans = max(ans, tmp)

print(ans)

