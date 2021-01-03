#print leap year between two given years
print("print leap year between two given years")
print("enter start year")
startyear=int(input())
print("enter last year")
lastyear=int(input())

print("list of leap years:")
for year in range(startyear,lastyear):
  if year%4==0:
    print(year)
