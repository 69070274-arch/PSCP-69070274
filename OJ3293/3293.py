"""frame"""
text = []
for i in range(5):
    x= input()
    text.append(x)

high = max(len(o) for o in text)

print("*"*(high+4))

for i in range(0,5):
    print(f"* {text[i]}{" "*(high - len(text[i])+1)}*")

print("*"*(high+4))
