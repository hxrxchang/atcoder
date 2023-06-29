import math

A, B = map(int, input().split())

lcm = A * B // math.gcd(A, B)

if lcm > 10 ** 18:
  print("Large")
else:
  print(lcm)
