H, W, N, H2, W2 = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(H)]

count = [0] * (N + 1)
num_of_kinds = 0

def count_kinds(count):
    result = 0
    for i in range(1, N + 1):
        if count[i] > 0:
            result += 1
    return result

for i in range(H):
    for j in range(W):
        n = A[i][j]
        if count[n] == 0:
            num_of_kinds += 1
        count[n] += 1

for h in range(H - H2 + 1):
    ans = []
    count2 = count[:]

    for i in range(h, h + H2):
        for j in range(W2):
            count2[A[i][j]] -= 1

    ans.append(count_kinds(count2))

    for w in range(1, W - W2 + 1):
        for i in range(h, h + H2):
            count2[A[i][w - 1]] += 1
            count2[A[i][w + W2 - 1]] -= 1
        ans.append(count_kinds(count2))

    print(*ans)
