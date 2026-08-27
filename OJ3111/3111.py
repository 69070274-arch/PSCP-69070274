"""kkk"""
from decimal import Decimal, ROUND_HALF_UP

M = input()
n = int(input())

total = Decimal("0")

for i in range(n):
    i+=0
    x = Decimal(input())
    total += x

if M == "Y":
    total = total - (total * Decimal("0.05"))

elif M == "N" and total >= Decimal("500"):
    total = total - (total * Decimal("0.03"))

total = total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

print(total)
