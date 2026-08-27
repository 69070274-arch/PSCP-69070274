"""santi"""
start, end = input().split()
weight = float(input())

if start == "BKK" and end == "CNX":
    BASE = 10
    RATE = 30

elif start == "CNX" and end == "UBP":
    BASE = 15
    RATE = 40

elif start == "UBP" and end == "BKK":
    BASE = 20
    RATE = 40

elif start == "BKK" and end == "PKT":
    BASE = 25
    RATE = 50

elif start == "PKT" and end == "CNX":
    BASE = 30
    RATE = 60

elif start == "UBP" and end == "PKT":
    BASE = 40
    RATE = 70

else:
    print("Error")
    BASE = 0
    RATE = 0

if BASE :
    total = BASE + weight * RATE
    print(f"{total:.2f}")
