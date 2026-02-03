def write_employee_record(name):
    record=f"""
    THIS IS TO CERTIFY THAT 
            {name}
    HAS COMPLETED GRADUATION SUCCESSFULLY
    AND WILL BE A ENGINEER FROM NOW ON
    """
    with open(f"{name}.txt","w") as f:
        f.write(record)

f = open("student.txt", "r")
a=f.read()
words=a.split()
for i in range(len(words)):
    write_employee_record(words[i])