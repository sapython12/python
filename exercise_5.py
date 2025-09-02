# 2) write a program to findout from which country user should buy IPhone. two countries are US & UK. assume person is indian. 

us_price = int(input("Enter the price of iPhone in US: "))
uk_price = int(input("Enter the price of iPhone in UK: "))
if us_price<uk_price:
    print("You should buy an iPhone from the US.")
else:
    print("You should buy an iPhone from the UK.")

print("Good Bye...")