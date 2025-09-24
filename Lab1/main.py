# write a program that prints hello world

print("Hello world")

# application to take a number in binary form from the user, and print it as a decimal


while True:
    num = input("Enter Binary number\n")
    try:
        num = int(num,2)
        break
    except ValueError:
        print("Enter binary only")
        
ans = int(num)
print(num)

# write a function that takes a number as an argument and if the number
    # divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is
    # divisible by both return "FizzBuzz"


x = 0
while True:
    num = input("Enter Integer number\n")
    try:
        num = int(num)
        x = num
        break
    except ValueError:
        print("Enter Integer only")
def chk(num):
    if num % 3 == 0 and num % 5 == 0 :
        return "FizzBuzz"
    elif num % 5 == 0:
        return "buzz"
    elif num % 3 == 0:
        return "Fizz"
    else:
        return "Not available"
ans = chk(x)
print(ans)

# Ask the user to enter the radius of a circle print its calculated area and circumference

import math 
r = 0
while True:
    num = input("Enter floating number\n")
    try:
        num = float(num)
        r = num
        break
    except ValueError:
        print("Enter floating only")
pi = math.pi
circumference = 2*pi*r
area = pi*(math.pow(r,2))
print("Circumference is : " , circumference)
print("Area is : " , area)


#	- Ask the user for his name then confirm that he has entered his name (not an empty string/integers). then proceed to ask him for his email and print all this data
name = input("Enter your name: ")
while not name.isalpha(): 
    print("enter a valid name")
    name = input("Enter your name: ")
email = input("Enter your email: ")
print("Your data:")
print("Name:", name)
print("Email:", email)

# - Write a program that prints the number of times the substring 'iti' occurs in a string
text = input("Enter a string: ")
count = text.count("iti")
print("Number of 'iti' is : ",count)
