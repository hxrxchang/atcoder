from collections import defaultdict

S = list(input())
T = list(input())
atc = 'atcoder'

S_dict = defaultdict(int)
T_dict = defaultdict(int)
for i in range(len(S)):
    S_dict[S[i]] += 1
    T_dict[T[i]] += 1

for s in atc:
    mx = max(S_dict[s], T_dict[s])
    if S_dict['@'] < mx - S_dict[s] or T_dict['@'] < mx - T_dict[s]:
        print('No')
        exit()
    S_dict['@'] -= mx - S_dict[s]
    S_dict[s] = mx
    T_dict['@'] -= mx - T_dict[s]
    T_dict[s] = mx

if S_dict == T_dict:
    print('Yes')
else:
    print('No')

