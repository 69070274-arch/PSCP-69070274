"""sssr"""
a = input()
num = ""
last = ""
a = a.lower()
if "a" in a:
    num = "ace"
elif "q" in a:
    num = "queen"
elif "j" in a:
    num = "jack"
elif "k" in a:
    num = "king"
else:
    num = a[0]

if "1" in a:
    num = "10"

if a[-1] == "d":
    last = "diamonds"
elif a[-1] == "h":
    last = "hearts"
elif a[-1] == "s":
    last = "spades"
elif a[-1] == "c":
    last = "clubs"

print(f"{num} of {last}")
