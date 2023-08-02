N = int(input())
S = list(input())

g = 0
ng = 0
for s in S:
    if s == "o":
        g += 1
    if s == "x":
        ng += 1

if g > 0 and ng == 0:
    print("Yes")
else:
    print("No")
