import csv
cols=['ID','Name','Place']
dictData1=[{'ID':1,'Name':'Manu','Place':'Muvattupuzha'},
           {'ID':2,'Name':'tuttu','Place':'Muvattupuzha'},
           {'ID':3,'Name':'Unni','Place':'Bangalore'},
           {'ID':4,'Name':'Saira','Place':'Bangalore'},
           {'ID':5,'Name':'Minnu','Place':'Ernakulam'}]
try:
    with open("Names.csv",'w')as file1:
        writer1=csv.DictWriter(file1,fieldnames=cols)
        writer1.writeheader()
        for data1 in dictData1:
            writer1.writerow(data1)
except IOError:
    print("I/O error")
data1=csv.DictReader(open("Names.csv"))
print("csv file as a dictionary:\n")
for row in data1:
    print(row)
           
