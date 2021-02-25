file1=input("enter the source file to be copied")
file2=input("enter the destination filename")
f1=open(file1,"r")
f2=open(file2,"w")
for line in f1.readline():
    f2.write(line)
f2.close()
f1.close()
