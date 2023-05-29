N = int(input())

restaurants = []
for _ in range(N):
  A, B = input().split()
  B = int(B)
  restaurants.append([A, B])
sorted_res = sorted(restaurants, key=lambda x: (x[0], -x[1]))

for res in sorted_res:
  print(restaurants.index(res) + 1)
