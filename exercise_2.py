age1 = int(input("Enter age of first brother: "))
age2 = int(input("Enter age of second brother: "))

if age1 > age2:
    print("First brother is elder")
if age2 > age1:
    print("Second brother is elder")
if age1 == age2:
    print("Both are of same age")