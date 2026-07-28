"""sdasd"""
a = int(input())
b = int(input())
goal = int(input())

big = goal // 5

if big > b:
    big = b

remain = goal - big * 5

if remain <= a:
    print(remain)
else:
    print(-1)
