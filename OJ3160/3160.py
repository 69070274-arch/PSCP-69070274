"""optimus"""
a, b = map(int, input().split())

count = 0

for n in range(a, b + 1):
    if n < 2:
        continue

    prime = True

    for i in range(2, n):
        if not n % i:
            prime = False
            break

    if prime:
        if count > 0:
            print(" ", end="")
        print(n, end="")
        count += 1

if count > 0:
    print()

print("Total primes:", count)
