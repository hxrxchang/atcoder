S = [int(x) for x in list(input())]
base = 753

tmp = S[:3]
for i in range(1, len(S) - 2):
    target = S[i:i+3]
    if abs(base - (tmp[0] * 100 + tmp[1] * 10 + tmp[2])) > abs(base - (target[0] * 100 + target[1] * 10 + target[2])):
        tmp = target

print(abs(base - (tmp[0] * 100 + tmp[1] * 10 + tmp[2])))
