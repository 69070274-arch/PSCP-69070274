"""s"""
import json

people = {}
dead = {}

while True:
    name = input()

    if name == "Start":
        break

    data = json.loads(name)
    people.update(data)

while True:
    name = input()

    if name == "End":
        break

    dead[name] = people[name]
    del people[name]

count = 0

for name, role in people.items():
    if role == "Impostor":
        count += 1

print(count, "Impostor Remains")
print("***Alive***")

for name in sorted(people):
    print(name, ":", people[name])

print("***Dead***")

for name in sorted(dead):
    print(name, ":", dead[name])
