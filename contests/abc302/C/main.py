import itertools

N, M = map(int, input().split())

S = [input() for _ in range(N)]

perms = itertools.permutations(S, N)

for strings in perms:
  flag = True
  # 組み合わせの検証
  for i in range(N - 1):
    # 前後の文字の検証
    A = strings[i]
    B = strings[i + 1]
    cnt = 0
    for i in range(M):
      if A[i] != B[i]:
        cnt += 1
    if cnt != 1:
      flag = False
      break
  if flag:
    print("Yes")
    exit()

print("No")


