"""nga"""
L, N = map(int, input().split())

total = 0
band = 1

while total < N:
    start = (band - 1) * L + 1
    end = band * L

    for i in range(start, end + 1):
        total += i

    if total >= N:
        break

    band += 1

print(band)
