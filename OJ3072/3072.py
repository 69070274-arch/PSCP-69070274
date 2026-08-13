text = input().lower()

aeiou = ["a", "e", "i", "o", "u"]
count = [0, 0, 0, 0, 0]

for i in text:
    if i == "a":
        count[0] += 1
    elif i == "e":
        count[1] += 1
    elif i == "i":
        count[2] += 1
    elif i == "o":
        count[3] += 1
    elif i == "u":
        count[4] += 1

for i in range(5):
    if count[i] > 0:
        print(aeiou[i], ":", count[i])
