"""castle"""
import math

N = int(input())

r = math.ceil(math.sqrt(N))

position = N - (r - 1) ** 2

if position % 2 == 1:
    print(2 * r - 2)
else:
    print(2 * r - 3)
