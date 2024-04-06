import math

N = int(input())

ans = ""

while N != 0:
    if N % -2 == 0:
        ans += "0"
    else:
        ans += "1"
    # 切り捨てじゃなくて切り上げなのは-2で割っているから？
    N = math.ceil(N / -2)

if ans == "":
    print(0)
else:
    ans = ans[::-1]
    print(ans)
