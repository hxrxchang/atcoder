from collections import deque
MOD = 998244353

N = int(input())
que = deque()
ans = 1
que.append(1)

for _ in range(N):
    Q = list(map(int, input().split()))
    if Q[0] == 1:
        que.append(Q[1])
        ans = (ans * 10 + Q[1]) % MOD
    elif Q[0] == 2:
        keta = len(que)
        top = que.popleft()
        ans -= top * pow(10, keta - 1, MOD)
        ans %= MOD
    elif Q[0] == 3:
        print(ans)
