N, K = map(int, input().split())
S = [int(input()) for _ in range(N)]

if 0 in S:
  print(N)
else:
  right = 0
  ans = 0
  tmp = 1
  for left in range(N):
    while right < N and tmp * S[right] <= K:
      tmp *= S[right]
      right += 1
    ans = max(ans, right - left)
    if left == right:
      right += 1
    else:
      tmp //= S[left]
  print(ans)
