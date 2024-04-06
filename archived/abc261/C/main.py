from collections import defaultdict

N = int(input())
S = defaultdict(int)

for i in range(N):
    s = input()
    if S[s] == 0:
        print(s)
    else:
        print(s + "(" + str(S[s]) + ")")
    S[s] += 1

