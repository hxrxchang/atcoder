from sys import stdin

N = int(stdin.readline())
sum_list = []
sub_list = []

for i in range(N):
  edge = list(map(int, stdin.readline().split()))
  x, y = edge[0], edge[1]
  sum_list.append(x + y)
  sub_list.append(x - y)

sum_list.sort()
sub_list.sort()

print(max(sum_list[-1] - sum_list[0], sub_list[-1] - sub_list[0]))
