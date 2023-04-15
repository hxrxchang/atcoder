N = int(input())
Q_ = int(input())

B = [[] for _ in range(N)]
B2 = [[] for _ in range(2 * 10 ** 5 + 1)]

def insert_into_sorted_list(sorted_list, new_element, remove_duplicate=False):
    # リストが空の場合、新しい要素を追加して終了
    if not sorted_list:
        sorted_list.append(new_element)
        return
    # 二分探索を用いて、新しい要素を挿入する場所を決定する
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == new_element:
            if remove_duplicate:
                return
            sorted_list.insert(mid, new_element)
            return
        elif sorted_list[mid] < new_element:
            left = mid + 1
        else:
            right = mid - 1

    sorted_list.insert(left, new_element)

for _ in range(Q_):
    Q = list(map(int, input().split()))
    if Q[0] == 1:
        insert_into_sorted_list(B[Q[2] - 1], Q[1])
        insert_into_sorted_list(B2[Q[1]], Q[2], remove_duplicate=True)
    elif Q[0] == 2:
        print(*B[Q[1] - 1])
    elif Q[0] == 3:
        print(*B2[Q[1]])

