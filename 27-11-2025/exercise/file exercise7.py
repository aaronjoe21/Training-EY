f=open("notes.txt","r")
for line in f:
    if "Python" in line:
        print(line)
