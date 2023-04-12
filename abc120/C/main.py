S = input()
N = len(S)
cnt = S.count('1')
cnt = min(cnt, N - cnt)

print(cnt * 2)
