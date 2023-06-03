import math
from collections import deque

N, D = map(int, input().split())

people = []
for i in range(N):
  people.append(list(map(int, input().split())))

infected = set()
infected_que = deque()

infected.add(0)
infected_que.append(0)

while infected_que:
  current = infected_que.popleft()
  X, Y = people[current][0], people[current][1]
  for i in range(N):
    if i in infected:
      continue
    x, y = people[i][0], people[i][1]
    if math.sqrt((X - x) ** 2 + (Y - y) ** 2) <= D:
      infected.add(i)
      infected_que.append(i)

for i in range(N):
  if i in infected:
    print('Yes')
  else:
    print('No')
