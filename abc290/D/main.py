T = int(input())

def solve(n, d, k):
  cnt = 1
  checked = [False] * n
  checked[0] = True
  last_checked = 0

  while cnt < k:
    nxt = (last_checked + d) % n
    while checked[nxt]:
      nxt = (nxt + 1) % n
    checked[nxt] = True
    last_checked = nxt
    cnt += 1

  print(last_checked)

def update_n(n):
  while n > 100:
    n = n // 100
  return n

for t in range(T):
  N, D, K = map(int, input().split())
  if N >= 100:
    N = update_n(N)
  if K >= 100:
    K = update_n(K)
  if D >= 100:
    D = update_n(D)
  solve(N, D, K)
