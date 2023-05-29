N = int(input())

restaurants = []
for i in range(N):
  A, B = input().split()
  B = int(B)
  restaurants.append([A, B, i + 1])
sorted_res = sorted(restaurants, key=lambda x: (x[0], -x[1]))

for res in sorted_res:
  print(res[2])
