N, A, B = map(int, input().split())

mod = 10 ** 9 + 7
def count(n, r):
    p, q = 1, 1
    for i in range(r):
        p = p * (n - i) % mod
        q = q * (i + 1) % mod
    # フェルマーの小定理
    return p * pow(q, mod - 2, mod) % mod

ans = pow(2, N, mod) - 1
ans -= count(N, A)
ans -= count(N, B)
ans %= mod

print(ans)

