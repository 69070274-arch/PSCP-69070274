"""sd"""
s = input()
result = ""

for i in s:
    if s.count(i) % 2 == 1 and i not in result:
        result += i

if not result:
    print("fully paired")
else:
    print(result)
