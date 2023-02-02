N, L = map(int, input().split())
K = int(input())
A = [0] + list(map(int, input().split())) + [L]

# checkを自力で実装したい
def check(x):
  left, right = 0, 0
  cnt = 0
  while right < len(A):
    if A[right] - A[left] >= x:
      cnt += 1
      left = right
      right += 1
    else:
      right += 1
  if cnt >= K + 1:
    return True
  return False

# 1cm ~ L+1cmの間でもっとも短いものの長さが最大になるものを二分探索
ok, ng = 1, L + 1
while ng - ok > 1:
  mid = (ok + ng) // 2
  if check(mid):
    ok = mid
  else:
    ng = mid

print(ok)
