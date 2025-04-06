import math

def ceil_div(n, d):
    return int((n + d - 1) // d)

N = int(input())

ans = 0
for a in range(1, 61):
    if pow(2, a) > N:
        break
    b = math.isqrt(N // pow(2, a))
    ans += ceil_div(b, 2)

print(ans)
