def words_frequent(n):
    a=n.split()
    dict={}
    for i in a:
        if i not in dict:
            dict[i]=1
        elif i in dict:
            dict[i]+=1
    print(dict)
n=input("Enter a sentence:")
words_frequent(n)
