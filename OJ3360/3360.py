"""sdd"""
W, H, M, N = map(int, input().split())

x = list(map(int, input().split()))
y = list(map(int, input().split()))

x.insert(0, 0)
x.append(W)

y.insert(0, 0)
y.append(H)

width = []
height = []

for i in range(M + 1):
    width.append(x[i + 1] - x[i])

for i in range(N + 1):
    height.append(y[i + 1] - y[i])

area = []

for w in width:
    for h in height:
        area.append(w * h)

area.sort()

print(area[-1], area[-2])
