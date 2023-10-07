import copy

N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [list(input()) for _ in range(N)]

current_status = [0] * N
not_solved = []

for i in range(N):
  cnt = 0
  not_solved_ = []
  for j, s in enumerate(S[i]):
    if s == "x":
      not_solved_.append(j)
    else:
      cnt += A[j]
  current_status[i] = cnt + i + 1
  not_solved.append(not_solved_)

A2 = []
for i in range(M):
  A2.append((i, A[i]))

A2.sort(key=lambda x: x[1], reverse=True)

for i in range(N):
  cnt = 0
  status = current_status[i]
  current_status2 = copy.deepcopy(current_status)
  current_status2.remove(status)
  maxi = max(current_status2)
  if status > maxi:
    print(cnt)
    continue
  for a in A2:
    if a[0] in not_solved[i]:
      cnt += 1
      status += a[1]
      if status > maxi:
        break
  print(cnt)
