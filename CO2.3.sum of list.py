#sum of elements in a list
list=input("enter a list:")
list1=map(int,list.split())
sum=0
for i in list1:sum+=i
print("the sum of all elements in list",list,"is",sum)

