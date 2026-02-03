n=input("Enter a string")
num=0
vowels=0
consonants=0
for i in n:
    if i.isdigit():
        num+=1
    elif i.isalpha():
        if i in "aeiouAEIOU":
            vowels+=1
        else:
            consonants+=1
print("Number of vowels: ",vowels)
print("Number of consonants: ",consonants)
print("Number of digits: ",num)