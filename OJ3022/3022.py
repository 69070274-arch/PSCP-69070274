"""temp"""
temp = float(input())
x = input()
y = input()
C = 0
ans = 0
if x == "C":
    C = temp
elif x == "F":
    C = (temp - 32) * 5 / 9
elif x == "K":
    C = temp - 273.15
elif x == "R":
    C = (temp - 491.67) * 5 / 9

if y == "C":
    ans = C
elif y == "F":
    ans = C * 9 / 5 + 32
elif y == "K":
    ans = C + 273.15
elif y == "R":
    ans = (C + 273.15) * 9 / 5

print(f"{ans:.2f}")