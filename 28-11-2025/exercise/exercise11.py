def write_employee_record(name):
    record=f"""
    Dear {name}
    Your training session starts tomorrow,
    Regards,
    Training Team
    """
    with open(f"EMAIL {name}.txt","w") as f:
        f.write(record)

f = open("names.txt", "r")
a=f.read()
words=a.split()
for i in range(len(words)):
    write_employee_record(words[i])