N, M, K = map(int, input().split())

if N > M:
    N, M = M, N

a = N * K
# a += K // M

print(a)
