from collections import defaultdict

K = int(input())

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

pf_list = prime_factorize(K)
pf_set = set(pf_list)
pf_dict = defaultdict(int)
for n in pf_list:
    pf_dict[n] = pf_dict[n] + 1

# nをpで何回割れるか
def how_many(n, p):
    res = 0
    while n % p == 0:
        n //= p
        res += 1
    return res

# 各素因数ごとに、素因数をその指数回割れる最小の数を探す
ans = 0
for p in pf_set:
    f = 0
    n = p
    while True:
        f += how_many(n, p)
        if f >= pf_dict[p]:
            ans = max(ans, n)
            break
        n += 1

print(ans)

