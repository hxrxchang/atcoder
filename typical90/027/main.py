N = int(input())

user_ids = set()

for i in range(N):
    user_id = input()
    if not user_id in user_ids:
        print(i + 1)
        user_ids.add(user_id)
