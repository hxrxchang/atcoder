a, b = map(int, input().split())
if 0 < a and 0 < b:
    print("Positive")
elif a < 0 and b < 0:
    if (b - a) % 2 == 0:
        print("Negative")
    else:
        print("Positive")
else:
    print("Zero")
