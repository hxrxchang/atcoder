M = int(input())
S = list(input())

memo = [0] * (M + 1)

for i in range(M):
    if S[i] == 'I':
        memo[i + 1] = memo[i] + 1
    else:
        memo[i + 1] = memo[i] - 1

print(max(memo))
