# Program to check if a number is prime or not

num = 29

# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable
flag = False

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
return 0;

import math
pi = math.pi
def circle(radius):
     return pi * radius**2
 
def cube(side):
     return side**3
 
def cylinder(radius, height):
     return 2*pi*radius + 2*pi*height
 
def sphere(radius):
     return 2*pi*(radius**2)
 
print(circle(10))
