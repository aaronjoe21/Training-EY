try:
    f=open("student.txt","r")
    print(f.read())
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission Denied")
