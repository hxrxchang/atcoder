N = int(input())
S = input()

if S.count('T') == S.count('A'):
    if S[0:N - 1].count('T') > S[0:N - 1].count('A'):
        print('T')
    else:
        print('A')
elif S.count('T') > S.count('A'):
    print('T')
else:
    print('A')
