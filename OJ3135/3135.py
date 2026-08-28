"""ooo"""
n, k, t = map(int, input().split())

x = 1
total = 0

while True:
    total += 1

    if x == t:
        break

    x = (x + k - 1) % n + 1

    if x == 1:
        break

print(total)
