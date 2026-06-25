#Program description: this program asks the user to input 3 integer values, representing the three sides of a triangle.
#It will then run 5 different functions to print off information about the triangle the user has entered. 
#In the start of the program this will ask user the informations of three sides

import math


side_a=int(input("Enter your first triangle side :"))
side_b=int(input("Enter your second triangle side :"))
side_c=int(input("Enter your third triangle side :"))
#This function shoould determine wether user's inputs is a triangle or not a triangle
def is_triangle():
    return side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a

#This function should dtermine wether user's inputs is a right triangle or not
def is_right_triangle():
    return side_a**2 + side_b**2 == side_c**2 or side_a**2 + side_c**2 == side_b**2 or side_b**2 + side_c**2 == side_a**2

#This function should calculate the perimeter of the triangle
def perimeter(a,b,c):
    perimeter = a + b + c
    return perimeter

#This function should scalculate the area of the triangle
def area():
    s = perimeter(side_a, side_b, side_c) / 2
    return math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))

#This function outputs the three sides of the triangle from smallest to largest
def display_triangle(a,b,c):
    smallest = a
    medium = b
    largest = c
    if smallest > medium:
        smallest, medium = medium, smallest
    if medium > largest:
        medium, largest = largest, medium
    if smallest > medium:
        smallest, medium = medium, smallest
    print("Smallest Side:", smallest)
    print("Medium Side:", medium)
    print("Largest Side:", largest)


if not is_triangle():
    print("The inputs you entered is not valid, they can't form a triangle")
    side_a=int(input("Enter your first triangle side"))
    side_b=int(input("Enter your second triangle side"))
    side_c=int(input("Enter your third triangle side"))
else :
    print("This is a true triangle.")

if is_right_triangle():
    print("This is a right triangle.")
else:
    print("This is not a right triangle")

print("The perimeter of the triangle is " + str(perimeter(side_a, side_b, side_c)))
print("The area of the triangle is " + str(area()))

display_triangle(side_a, side_b, side_c)
