import math

N = int(input())
x = N / 1.08

a = math.floor(x)
b = math.ceil(x)

if math.floor(a * 1.08) == N:
  print(a)
elif math.floor(b * 1.08) == N:
  print(b)
else:
  print(":(")
