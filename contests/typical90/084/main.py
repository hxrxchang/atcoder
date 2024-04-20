N = int(input())
S = input()

left = 0
# leftとして、S[i] を採用するときの組み合わせ数
# 例えば (1, 2), (1, 3) の組み合わせが有効な場合、S[1]は2になる
ans = [0] * N

for right in range(1, N):
    if S[left] == S[right]:
        continue

    # left から right まで見る。
    for l in range(left, right):
        # S[l とS[right]が異なる文字になればいい
        # したがってright以降はすべて採用できるので、 lを採用するときの組み合わせ数は S[right:] の個数になる
        ans[l] = len(S[right:])
    left = right

# S[-1] は left として採用できないため、最後は省く
print(sum(ans[:N - 1]))
