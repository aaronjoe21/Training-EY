with open("sample.txt", "r") as f:
    text = f.read()

chars = len(text)
words = len(text.split())
lines = text.count("\n") + 1

print("Characters:", chars)
print("Words:", words)
print("Lines:", lines)
