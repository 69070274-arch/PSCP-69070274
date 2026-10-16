"""sss"""
n, p = map(float, input().split())
n = int(n)

tile_col = [0] * n
point_col = [0] * n

total_tile = 0
total_point = 0

for i in range(n):
    i+=0
    a = list(map(int, input().split()))

    tile_row = 0
    point_row = 0

    for j in range(n):
        if a[j] > 0:
            tile_row += 1
            point_row += a[j]

            tile_col[j] += 1
            point_col[j] += a[j]

    total_tile += tile_row
    total_point += point_row

    print(*a, tile_row, point_row)

print(*tile_col)
print(*point_col)
print(total_tile, total_point, format(total_point * p, ".2f"))
