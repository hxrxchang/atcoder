N, L, R = map(int, input().split())
A = list(map(int, input().split()))

# i番目をLにするとき、i以降の数列の和の最小値
dpL = [0] * N
# i番目にA[i]を選ぶとき、i以降の数列の和の最小値
dpA = [0] * N
# i番目をRにするとき、i以降の数列の和の最小値
dpR = [R * (N - i) for i in range(N)]

dpA[-1] = A[-1]
dpL[-1] = L

for i in range(N - 1, 0, -1):
  dpA[i - 1] = A[i - 1] + min(dpA[i], dpR[i])
  dpL[i - 1] = L + min(dpL[i], dpA[i], dpR[i])

ans = min(dpA[0], dpL[0], dpR[0])
print(ans)
