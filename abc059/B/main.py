A = input()
B = input()

if A == B:
    print("EQUAL")
elif len(A) > len(B):
    print("GREATER")
elif len(B) > len(A):
    print("LESS")
else:
    numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    for i in range(len(A)):
        if int(A[i]) > int(B[i]):
            print("GREATER")
            break
        elif int(B[i]) > int(A[i]):
            print("LESS")
            break

# これでもいける
A = int(input())
B = int(input())

if A == B:
    print("EQUAL")
elif A > B:
    print("GREATER")
elif B > A:
    print("LESS")

