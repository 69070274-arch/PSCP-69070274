"""na"""
x = input()
y = input()
prize = ""
if x == y:
    prize = "1000000"
elif x[1:] == y[1:]:
    prize = "100000"
elif x[-3:] == y[-3:] and x[0] == y[0]:
    prize = "2000"
elif x[-2:] == y[-2:] and x[0] == y[0]:
    prize = "1000"
elif x[-3:] == y[-3:] and x[0] != y[0]:
    prize = "200"
elif x[-2:] == y[-2:] and x[0] != y[0]:
    prize = "100"
elif x[0] == y[0]:
    prize = "20"
else:
    prize = "0"
print(prize)
