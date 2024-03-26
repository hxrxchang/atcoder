N, K = map(int, input().split())

MOD = 10 ** 9 + 7

ans = 0
for i in range(K, N + 2):
    # 0~iまでの和
    start = i * (i - 1) // 2
    # N - i ~ Nまでの和
    end = (N * 2 - i + 1) * i // 2
    # 等差数列からN個選ぶ組み合わせは、和の最大と和の最小の差分 + 1を取ればよい
    ans += end - start + 1
    ans %= MOD

print(ans)



