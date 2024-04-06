N, K =map(int, input().split())
S = input()

cnt = 0
ans = ""
for i in range(N):
  if S[i] == "o" and cnt < K:
    ans += "o"
    cnt += 1
  else:
    ans += "x"

print(ans)
