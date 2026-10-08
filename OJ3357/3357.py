"""Ss"""
n = int(input())

height = []

for i in range(n):
    height.append(int(input()))

count = 0

for i in range(n):

    if n == 1:
        count += 1

    elif not i:
        if height[i] > height[i + 1]:
            count += 1

    elif i == n - 1:
        if height[i] > height[i - 1]:
            count += 1

    else:
        if height[i] > height[i - 1] and height[i] > height[i + 1]:
            count += 1

print(count)
