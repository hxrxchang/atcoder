from collections import defaultdict

def calc_divisors(N):
    # 答えを表す集合
    res = []

    # 各整数 i が N の約数かどうかを調べる
    for i in range(1, N + 1):
        # √N で打ち切り
        if i * i > N:
            break

        # i が N の約数でない場合はスキップ
        if N % i != 0:
            continue

        # i は約数である
        res.append(i)

        # N ÷ i も約数である (重複に注意)
        if N // i != i:
            res.append(N // i)

    # 約数を小さい順に並び替えて出力
    res.sort()
    return res

N = int(input())
A = list(map(int, input().split()))

dividors = defaultdict(list)
cnt = defaultdict(int)

for a in A:
    cnt[a] += 1
    if dividors[a] == []:
        dividors[a] = calc_divisors(a)

ans = 0
for i in dividors.keys():
    for j in dividors[i]:
        k = i // j
        ans += cnt[i] * cnt[j] * cnt[k]

print(ans)
