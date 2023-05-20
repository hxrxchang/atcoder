import math
from decimal import Decimal

A, B = map(int, input().split())
A, B = Decimal(A), B

ans = A / B

if ans % 1 == 0:
  print(int(ans))
else:
  print(math.ceil(ans))
