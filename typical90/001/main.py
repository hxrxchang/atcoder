N, L = map(int, input().split())
K = int(input())
A = [0] + list(map(int, input().split())) + [L]

# Aを左から順番に調べて、xより大きいものを取り出してその数を調べる
def check(x):
  left, right = 0, 1
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

# 1cm ~ Lcmの間でもっとも短いものの長さが最大になるものを二分探索
ok, ng = 1, L
while ng - ok > 1:
  mid = (ok + ng) // 2
  if check(mid):
    ok = mid
  else:
    ng = mid

print(ok)
