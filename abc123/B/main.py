from itertools import permutations

dishes = [int(input()) for _ in range(5)]

ans = float('inf')
for permutation in permutations(dishes):
    cnt = 0
    for dish in permutation:
        if cnt % 10 != 0:
            cnt += 10 - (cnt % 10)
        cnt += dish
    if cnt < ans:
        ans = cnt

print(ans)

