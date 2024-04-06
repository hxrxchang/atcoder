import itertools

N = int(input())
runners_time = [list(map(int, input().split())) for _ in range(N)]

M = int(input())
runners_dislike = {i: set() for i in range(N)}
for _ in range(M):
  A, B = map(int, input().split())
  runners_dislike[A - 1].add(B - 1)
  runners_dislike[B - 1].add(A - 1)

# 選手の並び順で仲が悪いペアがあるかどうかをチェックする
def check_ok(runners_perm):
  for i in range(len(runners_perm) - 1):
    A, B = runners_perm[i], runners_perm[i + 1]
    if B in runners_dislike[A]:
      return False
  return True


runners = [i for i in range(N)]
ans = float('inf')
for perm in itertools.permutations(runners, N):
  if not check_ok(perm):
    continue
  time = 0
  for i, runner in enumerate(perm):
    time += runners_time[runner][i]
  ans = min(ans, time)

if ans == float('inf'):
  print(-1)
else:
  print(ans)
