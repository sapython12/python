year = int(input("Enter a year: "))

if year % 1000 == 0:
    print(year, "is a millennium year")
if year % 1000 != 0:
    print(year, "is not a millennium year")