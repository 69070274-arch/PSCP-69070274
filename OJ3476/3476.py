"""sss"""
import json

N = int(input())
DICT = {}

for _ in range(N):
    data = json.loads(input())
    DICT.update(data)

if "Cat01" not in DICT.values() and "Garfield" not in DICT:
    DICT.update({"Garfield": "Cat01"})

if "Fox01" not in DICT.values() and "Fubuki" not in DICT:
    DICT.update({"Fubuki": "Fox01"})

cats = []
foxs = []

for name, number in DICT.items():
    if number.startswith("Cat"):
        cats.append([name, number])
    else:
        foxs.append([name, number])

cats.sort(key=lambda x: int(x[1][3:]))
foxs.sort(key=lambda x: int(x[1][3:]))

print("Cat :", len(cats))
print("Fox :", len(foxs))

for name, number in cats:
    print(name, ":", number)

for name, number in foxs:
    print(name, ":", number)
