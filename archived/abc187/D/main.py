N = int(input())
# 高橋くんの青木くんとの獲得票数の差。高橋くんが勝っている場合は正の値、青木くんが勝っている場合は負の値
point_diff = 0
towns_vote_data = []

for _ in range(N):
  A, B = map(int, input().split())
  towns_vote_data.append([A, B, 2 * A + B])
  point_diff -= A

towns_vote_data.sort(key=lambda x: x[2], reverse=True)

for i, town in enumerate(towns_vote_data):
  # 高橋くんはA, B両方の票を獲得することができ、青木くんはAの票数を失うので、town[0] * 2 する。
  point_diff += town[0] * 2 + town[1]
  if point_diff > 0:
    print(i + 1)
    break
