import datetime
with open("student.txt","r") as f:
    user=f.read()
    names=user.split()
    with open("attendance.txt","a+") as c:
        for name in names:
            Attendance = input(f"Enter attendance for {name}: ")
            c.write(f""" Date&Time: {datetime.datetime.now().strftime('%H:%M:%S')}
            Name: {name}
            Attendance:{Attendance}
            -----------------------------------------\n""")
        c.seek(0)
        print(c.read())