N = int(input())
S = list(input())

cnt = 0
for i, s in enumerate(S):
    if s == 'c':
        cnt += 2 * (2 ** i)
    elif s == 'b':
        cnt += 2 ** i

print(cnt)
