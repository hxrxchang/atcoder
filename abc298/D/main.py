Q_ = int(input())
S = [1]
sum = '1'

for _ in range(Q_):
    Q = list(map(int, input().split()))
    if Q[0] == 1:
        S.append(Q[1])
        sum += str(Q[1])
    elif Q[0] == 2:
        p = S.pop(0)
        sum = sum[1:]
    elif Q[0] == 3:
        print(int(sum) % 998244353)
