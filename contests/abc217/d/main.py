from sortedcontainers import SortedSet

L, Q = map(int, input().split())
cut = SortedSet()

for _ in range(Q):
    q, x = map(int, input().split())
    if q == 1:
        cut.add(x)
    else:
        if len(cut) == 0:
            print(L)
            continue
        # xより小さい値の中で最大のもののindex
        l = cut.bisect_left(x) - 1
        # x以上の値の中で最小のもののindex
        r = cut.bisect_left(x)
        if cut[l] > x:
            left = 0
        else:
            left = cut[l]
        if r >= len(cut):
            right = L
        else:
            right = cut[r]

        print(right - left)
