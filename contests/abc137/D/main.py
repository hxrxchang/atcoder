from heapq import heappop, heappush

N, M = map(int, input().split())

# 仕事を何日後(M日)にいくらの報酬を得られるかを表す
# 1次元目がM日、2次元目がいくらか
# 1 <= A, A <= 10 ** 5 なので [0] は空のままだが、扱いやすいのでそのままにする。
rewards_per_days = [[] for _ in range(M + 1)]

for _ in range(N):
  A, B = map(int, input().split())
  if A > M:
    continue
  rewards_per_days[A].append(B)

cnt = 0
que = []
# M-1日から考えると、Aが1である仕事の中から報酬が最大のものを選べばいいことがわかる。
# M-2日、M-3日と過去に遡っていくが、heapから最大の報酬を選べばいい。
for rewards in rewards_per_days:
  for reward in rewards:
    # pythonのheapは小さい順に取り出されるので、最大値を取り出したい場合は符号を逆転して保存する
    heappush(que, -reward)
  if que:
    # 符号が逆転されて保存されているので、さらに逆転させて元に戻す
    reward = -heappop(que)
    cnt += reward

print(cnt)


