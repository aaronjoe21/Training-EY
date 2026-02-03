n=input("Enter a sentence: ")
try:
    f=open("name.txt","w+")
    f.write(n)
except FileNotFoundError:
    print("File not exist")
else:
    f.seek(0)
    print(f.read())
finally:
    print("Done")

