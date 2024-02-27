N, S = map(int, input().split())
cards = [tuple(map(int, input().split())) for _ in range(N)]

# dp[i][j] = i番目までのカードでjを作れるか
dp = [[False] * (S + 1) for _ in range(N + 1)]
dp[0][0] = True

for i in range(1, N + 1):
    for j in range(S + 1):
        card = cards[i - 1]
        ja, jb = j - card[0], j - card[1]
        if ja >= 0 and dp[i - 1][ja]:
            dp[i][j] = True
        if jb >= 0 and dp[i - 1][jb]:
            dp[i][j] = True

if not dp[-1][-1]:
    print("No")
    exit()

print("Yes")
selected = []
cnt = S
for i in range(N, 0, -1):
    h, t = cards[i - 1][0], cards[i - 1][1]
    if dp[i - 1][cnt - h]:
        selected.append("H")
        cnt -= h
    else:
        selected.append("T")
        cnt -= t

print("".join(selected[::-1]))
