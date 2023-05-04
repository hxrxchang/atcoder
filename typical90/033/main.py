import math

H, W = map(int, input().split())

if H == 1 or W == 1:
    print(H * W)
    exit()

H = math.ceil(H / 2)
W = math.ceil(W / 2)

print(H * W)
