"""shorten"""
numbers = []

while True:
    n = int(input())

    if n == -1:
        break

    numbers.append(n)

result = []
i = 0

while i < len(numbers):
    start = numbers[i]
    end = start

    while i + 1 < len(numbers) and numbers[i + 1] == numbers[i] + 1:
        i += 1
        end = numbers[i]

    if start == end:
        result.append(str(start))
    else:
        result.append(str(start) + "-" + str(end))

    i += 1

print(", ".join(result))
