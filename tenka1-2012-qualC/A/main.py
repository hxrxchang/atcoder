N = int(input())

def Eratosthenes(n):
    is_prime_table = [True] * (n + 1)
    # 0, 1 は予めふるい落としておく
    is_prime_table[0], is_prime_table[1] = False, False
    # ふるい
    for p in range(2, n + 1):
        # すでに合成数であるものはスキップする
        if not is_prime_table[p]:
            continue
        # p 以外の p の倍数から素数ラベルを剥奪
        q = p * 2
        while q <= n:
            is_prime_table[q] = False
            q += p
    return is_prime_table

# Nより小さいなので、末尾は除く
ans = Eratosthenes(N)[0:-1].count(True)
print(ans)

