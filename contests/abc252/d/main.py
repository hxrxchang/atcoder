N = int(input())
A = list(map(int, input().split()))

# A[i] < A[j] < A[k] となるような組み合わせの数を求める
# A[j] について考えて、A[j] より小さい数と A[j] より大きい数の数を数えればOK
limit = max(A)
cnt = [0] * (limit + 1)
# 各要素の出現回数を求める
for a in A:
    cnt[a] += 1

# cnt[i]: Aにi以下の数がいくつあるかを計算
for i in range(limit):
    cnt[i + 1] += cnt[i]

ans = 0
for a in A:
    countLessThanA = cnt[a-1]
    countGreaterThanA = N - cnt[a]
    ans += countLessThanA * countGreaterThanA

print(ans)

