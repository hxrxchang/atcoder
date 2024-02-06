S = list(input())
N = int(input())

bitToNumMap = {}
for i in range(1, 61):
    bitToNumMap[i] = (2 ** (i - 1))

cnt = 0
for i in range(len(S)):
    j = len(S) - i
    if S[i] == "1":
        cnt += bitToNumMap[j]

if cnt > N:
    print(-1)
    exit()

for i in range(len(S)):
    j = len(S) - i
    if S[i] == "?":
        if cnt + bitToNumMap[j] <= N:
            cnt += bitToNumMap[j]

print(cnt)


