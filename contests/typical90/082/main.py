MOD = 10 ** 9 + 7
L, R = map(int, input().split())

# Lの桁数
l_digit = len(str(L))
# Rの桁数
r_digit = len(str(R))

ans = 0
# Lの桁数からRの桁数まで各桁を考える
for i in range(l_digit, r_digit + 1):
    # 例えばi=1のとき、min_numは Lまたは1のどちらか大きい方、max_numは Rまたは9のどちらか小さい方になる
    min_num = max(L, 10 ** (i - 1))
    max_num = min(R, 10 ** i - 1)

    num = max_num - min_num + 1

    # 初項、末項、項数が分かるときの等差数列の和の公式を使って、min_numからmax_numまでの和を求める
    # 桁数でかけるかけることで、文字の個数を求める
    ans += (num * (min_num + max_num) // 2) * i
    ans %= MOD

print(ans)
