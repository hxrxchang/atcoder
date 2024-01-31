from collections import defaultdict
import bisect


def count_elements_in_range_bisect(arr, low_value, high_value):
    lower_bound_index = bisect.bisect_left(arr, low_value)
    upper_bound_index = bisect.bisect_right(arr, high_value)
    return upper_bound_index - lower_bound_index

N = int(input())
A = list(map(int, input().split()))

Q = int(input())
memo = defaultdict(list)

for i, a in enumerate(A):
    memo[a].append(i)

for _ in range(Q):
    L, R, X = map(int, input().split())
    L -= 1
    R -= 1
    print(count_elements_in_range_bisect(memo[X], L, R))
