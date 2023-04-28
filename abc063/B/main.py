S = list(input())

strigs = set()

for s in S:
    if s in strigs:
        print('no')
        exit()
    else:
        strigs.add(s)

print("yes")
