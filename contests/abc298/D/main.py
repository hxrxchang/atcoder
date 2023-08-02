from collections import deque

mod = 998244353
Q_ = int(input())
que = deque()
ans = 1
que.append(1)
for _ in range(Q_):
    Q = list(map(int, input().split()))
    if Q[0] == 1:
        que.append(Q[1])
        ans = (ans * 10 + Q[1]) % mod
    elif Q[0] == 2:
        keta = len(que)
        top_el = que.popleft()
        ans -= top_el * pow(10, keta - 1, mod) % mod
        ans %= mod
    elif Q[0] == 3:
        print(ans)
