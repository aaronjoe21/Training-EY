def questions(question):
    return f"Question{num} :{question}? \nAnswer:\n\n\n"
num=1
with open("quiz.txt","a+") as file:
    while True:
        num += 1
        n = (input("Do you want add a question?(Y/N)"))
        if n=="Y":
            file.write(questions(input("Enter your question:")))
        else:
            break