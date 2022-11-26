# WIP
import math

num = 100000

A, B = map(int, input().split())
g = 1
temp = []
time = 0
while True:
  g += num
  time += B * num
  a = time + A * math.sqrt(g) / g
  if not len(temp):
    temp.append(a)
    continue
  if len(temp) and a < temp[-1]:
    temp.append(a)
  else:
    break

if len(temp) < 2:
  g2 = 1
  time2 = 0
  temp2 = A
else:
  g2 = g - num
  time2 = time - num
  temp2 = temp[-2]

for _ in range(num):
  g2 += 1
  time2 += time
  a = time2 + A * math.sqrt(g2) / g2
  if a <= temp2:
    temp2 = a
  else:
    break

print(temp2)



