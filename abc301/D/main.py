from copy import deepcopy

S = list(input())
N = int(input())

idx = []
for i in range(len(S)):
    if S[i] == '?':
        idx.append(i)

data = []

for i in range(2 ** len(idx)):
    S_ = deepcopy(S)
    for j in range(len(idx)):
        if (i >> j) & 1:
            S_[idx[j]] = '1'
        else:
            S_[idx[j]] = '0'
    S_ = ''.join(S_)
    data.append(int(S_, 2))

data.sort()

tmp = -1
for d in data:
    if d > N:
        print(tmp)
        exit()
    if d <= N:
        if d > tmp:
            tmp = d

print(tmp)
