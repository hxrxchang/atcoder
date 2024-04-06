N = int(input())
persons = []

mini = float('inf')
mini_idx = float('inf')
for i in range(N):
  S, A = input().split()
  A = int(A)
  if A < mini:
    mini = A
    mini_idx = i
  persons.append((S, A))

for i in range(N):
  idx = mini_idx + i
  if idx > N - 1:
    idx -= N
  print(persons[idx][0])
