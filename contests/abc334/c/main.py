"""AtCoder Beginner Contest 334 C"""
import sys

INF = 1 << 30

n, k = map(int, input().split())
a = list(map(int, input().split()))

if k % 2 == 0:
    result = 0
    for i in range(k // 2):
        result += a[2 * i + 1] - a[2 * i]
    print(result)
    sys.exit()

s_left = [0] * (k // 2 + 1)
s_left[0] = 0
for i in range(k // 2):
    s_left[i + 1] = s_left[i] + a[2 * i + 1] - a[2 * i]
s_right = [0] * (k // 2 + 1)
s_right[0] = 0
for i in range(k // 2):
    s_right[i + 1] = s_right[i] + a[k - 1 - (2 * i)] - a[k - 1 - (2 * i + 1)]

print(s_left)
print(s_right)

result = INF
for i in range(k // 2 + 1):
    result = min(result, s_left[i] + s_right[k // 2 - i])

print(result)
