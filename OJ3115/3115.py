"""arcade"""
num, check = map(int, input().split())

time = [0] * 1441

for i in range(num):
    start, stop = map(int, input().split())
    time[start] += 1
    time[stop] -= 1

for i in range(1, 1441):
    time[i] += time[i - 1]

check_time = map(int, input().split())

answer = []

for t in check_time:
    answer.append(str(time[t]))
check+=0
print(" ".join(answer))
