f=open("sources.txt","w+")
f.write("Gods Own country - Kerala")
f.seek(0)
content=f.read()
f.close()

a=open("backup.txt","w+")
a.write(content)
a.close()
