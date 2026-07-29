"""bilibili"""
og = int(input())
service = og * 0.1
if service < 50:
    service = 50
elif service > 1000:
    service = 1000
total = (og + service) * 1.07
print(f"{total:.2f}")
