from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = defaultdict(int)
right = 0
ans = 0
tmp_elements = 0

for left in range(N):
  while right < N and tmp_elements <= K:
    if cnt[A[right]] == 0:
      tmp_elements += 1
    cnt[A[right]] += 1
    right += 1

  if tmp_elements <= K:
    ans = max(ans, right - left)
  else:
    ans = max(ans, right - left - 1)

    cnt[A[left]] -= 1
    if cnt[A[left]] == 0:
      tmp_elements -= 1

print(ans)
