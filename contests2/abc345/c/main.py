from collections import defaultdict

S = input()
res = [0] * len(S)
ruiseki = 0
# 後ろから見ていったときに各文字が何個でてきたか
d = defaultdict(int)

for i in range(len(S) - 1, -1, -1):
    res[i] = ruiseki - d[S[i]]
    ruiseki += 1
    d[S[i]] += 1

if len(d.keys()) == 1:
    print(1)
    exit()

ans = 0
for r in res:
    ans += r

print(ans)
