from heapq import heappush, heappop

N, M = map(int, input().split())
AtoB = [[] for _ in range(M + 1)]

for _ in range(N):
  A, B = map(int, input().split())
  if A > M:
    continue
  AtoB[A].append(B)

ans = 0
que = []

for B in AtoB:
  for b in B:
    # pythonのヒープは小さい順なので、符号反転して追加(絶対値の大きさで取得する)
    heappush(que, -b)
  if que:
    # 反転した符号を戻す
    a = -heappop(que)
    ans += a

print(ans)
