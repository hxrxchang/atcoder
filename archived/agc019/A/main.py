Q, H, S, D = map(int, input().split())
N = int(input())

one_l = min(Q * 4, H * 2, S)

ans = min(one_l * N, D * (N // 2) + one_l * (N % 2))
print(ans)
