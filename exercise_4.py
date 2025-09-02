# 1) write a program to findout which triangle is bigger from 2 triangle. accept base and height from user. 

triangle1_base = int(input("Enter base of triangle 1: "))
triangle1_height = int(input("Enter height of triangle 1: "))
triangle2_base = int(input("Enter base of triangle 2: "))
triangle2_height = int(input("Enter height of triangle 2: "))

area1 = 1/2 * triangle1_base * triangle1_height
area2 = 1/2 * triangle2_base * triangle2_height
if area1>area2:
    print("Triangle 1 is bigger")
else:
    print("Triangle 2 is bigger")

print("Good Bye...")