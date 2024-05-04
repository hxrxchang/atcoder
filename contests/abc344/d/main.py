T = input()
N = int(input())

bags = [list(map(int, input().split())) for _ in range(N)]

dp = [(0, 0)] * (len(T) + 1)

for i in range(N):

