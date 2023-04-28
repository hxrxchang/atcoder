A, B = map(int, input().split())
S = input()

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in range(A):
    if S[i] not in numbers:
        print('No')
        exit()

if S[A] != '-':
    print('No')
    exit()

for i in range(A + 1, A + B + 1):
    if S[i] not in numbers:
        print('No')
        exit()

print('Yes')
