str1=input("Enter the first string:")
str2=input("Enter the second string:")
new_a=str2[:2]+str1[2:]
new_b=str1[:2]+str2[2:]
print("The new string after swapping first two characters of both string:",(new_a+' '+new_b))
