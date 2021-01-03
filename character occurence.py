#character occurence
Astr=input("enter the string\n")
char=input("enter the character\n")
print("given string:",Astr)
print("given character",char)
res=0
for i in range(len(Astr)):
            
    if(Astr[i]==char):
        
        res=res+1
        
print("no of time character is present in the string\n",res)
