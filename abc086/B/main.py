import math

a, b = input().split()
v = math.sqrt(int(a + b))

if v - math.floor(v) == 0:
  print("Yes")
else:
  print("No")
