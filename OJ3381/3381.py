"""sss"""
T = int(input())

for i in range(T):
    i+=0
    N = int(input())
    points = []

    for j in range(N):
        j+=0
        x, y = map(int, input().split())
        points.append((x, y))

    for j in range(N):
        j+=0
        for k in range(N - 1):
            sum1 = points[k][0] + points[k][1]
            sum2 = points[k + 1][0] + points[k + 1][1]

            if sum1 > sum2:
                points[k], points[k + 1] = points[k + 1], points[k]

            elif sum1 == sum2:
                if points[k][1] < points[k + 1][1]:
                    points[k], points[k + 1] = points[k + 1], points[k]

    for x, y in points:
        print(x, y)
