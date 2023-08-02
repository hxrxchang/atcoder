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
    # 文字数が少ない方を多い方にあわせるように処理する。
    # そうする理由は、多い方を少ない方にあわせると、減らした文字を他の文字に振り分ける必要があるが、どうすればいいかわからないから。
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

