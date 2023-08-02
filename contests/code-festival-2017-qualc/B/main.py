N = int(input())
A = list(map(int, input().split()))

pattern = 3 ** N

all_odd = 1
for a in A:
  if a % 2 == 1:
    all_odd *= 1
  else:
    all_odd *= 2

print(pattern - all_odd)
