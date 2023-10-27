N, M = map(int, input().split())
problems = []
for _ in range(M):
  p, s = input().split()
  problems.append((int(p), s))

solved = [False] * (N + 1)
wa_cnt = [0] * (N + 1)
for problem in problems:
  problem_id = problem[0]
  result = problem[1]
  if result == 'AC':
    solved[problem_id] = True
  else:
    if not solved[problem_id]:
      wa_cnt[problem_id] += 1

AC_cnt = 0
penalty_cnt = 0
for i in range(1, N + 1):
  if solved[i]:
    AC_cnt += 1
    penalty_cnt += wa_cnt[i]

print(AC_cnt, penalty_cnt)
