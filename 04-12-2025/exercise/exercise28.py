with open("sample.txt", "r") as f:
    lines = f.readlines()

mid = len(lines) // 2
with open("first_half.txt", "w") as f1, open("second_half.txt", "w") as f2:
    f1.writelines(lines[:mid])
    f2.writelines(lines[mid:])
