import math

data = list(map(int, input().split()))
data.sort()

if data[0] % 2 == 0 or data[1] % 2 == 0 or data[2] % 2 == 0:
  print(0)
else:
  print(data[0] * data[1] * math.ceil(data[2] / 2) - data[0] * data[1] * (data[2] // 2))
