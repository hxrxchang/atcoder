from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = defaultdict(int)
elements = 0
ans = 0
right = 0

for left in range(N):
  while right < N and elements <= K:
    cnt[A[right]] += 1
    elements += 1
    right += 1

  if elements <= K:
    ans = max(ans, right - left)
  else:
    ans = max(ans, right - left - 1)

  cnt[A[left]] -= 1
  if cnt[A[left]] == 0:
    elements -= 1
    del cnt[A[left]]

print(ans)
