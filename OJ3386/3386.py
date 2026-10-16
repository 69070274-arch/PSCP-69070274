"""sss"""
m = int(input())
n = int(input())
a = []
b = []
result = []

for i in range(m):
    a.append(int(input()))

for i in range(n):
    b.append(int(input()))

for i in a:
    if i in b and i not in result:
        result.append(i)

result.sort(reverse=True)

if not result:
    print("Nope")
else:
    for i in result:
        print(i)
