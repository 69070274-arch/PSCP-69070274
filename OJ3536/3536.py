"""sss"""
n = int(input())

if n < 2:
    print("NO")
else:
    prime = True

    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            prime = False
            break

    if prime:
        print("YES")
    else:
        print("NO")
