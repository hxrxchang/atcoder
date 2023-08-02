N = int(input())
C = input()
red_cnt = C.count("R")
left = C[:red_cnt]
ans = left.count("W")

print(ans)

