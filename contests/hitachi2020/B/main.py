A_, B_, M_ = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

coupons = [list(map(int, input().split())) for _ in range(M_)]

ans = min(A) + min(B)

for coupon in coupons:
    a, b, c = coupon
    ans = min(ans, A[a - 1] + B[b - 1] - c)

print(ans)
