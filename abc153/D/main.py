import math
H = int(input())

total = 0
number = 1

while number <= H:
    total += number
    number *= 2

print(total)
