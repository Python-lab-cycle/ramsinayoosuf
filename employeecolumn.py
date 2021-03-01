import csv
with open('Employee1.csv',newline='')as csvfile1:
    data=csv.DictReader(csvfile1)
    print('empno empname')
    print("--------------")
    for i in data:
        print(i['Empno'],i['Empname'])
