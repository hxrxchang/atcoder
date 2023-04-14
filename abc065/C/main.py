import math

N, M = map(int, input().split())
if abs(N - M) > 1:
    print(0)
    exit()

ans = math.factorial(N) * math.factorial(M)

if N == M:
    ans *= 2

ans %= 10 ** 9 + 7

print(ans)
