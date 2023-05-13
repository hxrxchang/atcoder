from collections import defaultdict
from string import ascii_lowercase

S = list(input())
T = list(input())
atc = 'atcoder'

S_dict = defaultdict(int)
T_dict = defaultdict(int)
for i in range(len(S)):
    S_dict[S[i]] += 1
    T_dict[T[i]] += 1

for s in list(ascii_lowercase):
    diff = abs(S_dict[s] - T_dict[s])
    if diff == 0:
        continue
    if s not in atc or (S_dict['@'] == 0 and T_dict['@'] == 0 and diff <= max(S_dict['@'], T_dict['@'])):
        print("No")
        exit()
    if S_dict['@'] >= T_dict['@']:
        S_dict['@'] -= diff
    else:
        T_dict['@'] -= diff

print("Yes")
