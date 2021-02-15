class bank():
    def __init__(self,acnt,name,types):
        self.ac=acnt
        self.nm=name
        self.typ=types
        self.bal=0
    def prntdtls(self):
        print("Account Holder Name:",self.nm)
        print("Account Number:",self.ac)
        print("Account Type:",self.typ)
    def deposit(self,d1):
        self.bal=self.bal+d1
        return(self.bal)
    def withdrw(self,w1):
        self.bal=self.bal-w1
        return(self.bal)
n=input("Enter Name:")
t=input("Enter type:")
num=int(input("Enter Account Number:"))
obj=bank(num,n,t)
print("Account Details")
print("****************")
obj.prntdtls()
while[True]:
    print("\n*****Menu*****")
    print("\n1.Deposit")
    print("\n2.withdraw")
    choice=int(input("enter choice:"))
    if(choice==1):
        d=int(input("Enter ammount to deposit:"))
        print("Balance Amount:",obj.deposit(d))
    elif(choice==2):
        w=int(input("Enter ammount to withdraw:"))
        print("Balance Amount:",obj.withdrw(w))
    else:
        print("Give a valid choice")
            
    
