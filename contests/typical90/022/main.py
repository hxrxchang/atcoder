import math

A, B, C = map(int, input().split())
gcd = math.gcd(math.gcd(A, B), C)

ans = (A // gcd - 1) + (B // gcd - 1) + (C // gcd - 1)

print(ans)
