N = int(input())
sum_of_students_scores_1 = [0] * (N + 1)
sum_of_students_scores_2 = [0] * (N + 1)

for i in range(1, N + 1):
  cls, score = map(int, input().split())
  if cls == 1:
    sum_of_students_scores_1[i] = sum_of_students_scores_1[i - 1] + score
    sum_of_students_scores_2[i] = sum_of_students_scores_2[i - 1]
  else:
    sum_of_students_scores_1[i] = sum_of_students_scores_1[i - 1]
    sum_of_students_scores_2[i] = sum_of_students_scores_2[i - 1] + score

# print(sum_of_students_scores_1)
# print(sum_of_students_scores_2)

Q = int(input())
for _ in range(Q):
  L, R = map(int, input().split())
  cls_1_score = sum_of_students_scores_1[R] - sum_of_students_scores_1[L - 1]
  cls_2_score = sum_of_students_scores_2[R] - sum_of_students_scores_2[L - 1]
  print(cls_1_score, cls_2_score)
