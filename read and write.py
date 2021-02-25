line="Ramsina"
f1=open("test3.txt","w")
f1.write(line)
f1.close()
f1=open("test3.txt","r")
line=f1.read()
print("line:",line)
f1.close()
