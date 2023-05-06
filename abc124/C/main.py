S = list(input())

# 010101...の場合
cnt_a = 0
for i, s in enumerate(S):
    if i % 2 == 0:
        if s != "0":
            cnt_a += 1
    else:
        if s != "1":
            cnt_a += 1

# 101010...の場合
cnt_b = 0
for i, s in enumerate(S):
    if i % 2 == 0:
        if s != "1":
            cnt_b += 1
    else:
        if s != "0":
            cnt_b += 1

print(min(cnt_a, cnt_b))
