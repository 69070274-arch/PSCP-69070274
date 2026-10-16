"""sss"""
n, s = map(int, input().split())

a = []

for i in range(n):
    i += 0
    a.append(int(input()))

visited = []
now = s
count = 0

while now and now not in visited:
    visited.append(now)
    count += 1
    now = a[now - 1]

print(count)
