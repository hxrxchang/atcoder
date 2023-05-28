N, M = map(int, input().split())

persons = [[] for _ in range(N + 1)]
for _ in range(M):
  A = list(map(int, input().split()))
  for i in range(N):
    if i - 1 >= 0:
      persons[A[i]].append(A[i - 1])
    if i + 1 < N:
      persons[A[i]].append(A[i + 1])

cnt = set()
for i in range(1, N + 1):
  person = persons[i]
  for j in range(1, N + 1):
    if j not in person and j != i:
      if i > j:
        cnt.add(str(j) + ":" + str(i))
      else:
        cnt.add(str(i) + ":" + str(j))

print(len(cnt))
