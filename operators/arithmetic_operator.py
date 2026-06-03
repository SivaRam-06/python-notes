'''
operators:
They are either special symbols or keywords used to operate on operands 
belonging to specific data types.

1. Arithmetic operators 
2. Relational operators
3. Logical operators
4. assignment operators
5. Membership operators
6. Idenntity operators
7. Bitwise operator
'''
'''
1.Arthmetic operators:
   > these are special symbols used for mathematical operations
     + - addition
     - - subtraction
     * - Multiplication
     / - Division
     //- Floor division (Integral division)-returns only quotient
     % - Modulus 
     ** - Exponent 

#where to use arithmetic operators in the program?
> used in mathematical calculations

#how to identify arithmetic operators are usedin the programs?
> by looking for the presence of symbols like +, -, *, /, //, %, ** in the code

a=18
b=4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

#write a program to find the sum of two given numbers 
a=int(input('Enter first number: '))
b=int(input("Enter  the second number:"))
sum=a+b
print("sum of two numbers is :",sum)
 

# write a program to find the area of the circle with given radius
# consider  pi =3.14
r=float(input("Enter the radius:"))
pi=3.14
area_of_circle=pi*(r**2)
print("area of circle is :",area_of_circle)'''

# write a program to find the square root of given number 
n=(int(input("Enter the number :")))
sqrt=(n**0.5)
print(sqrt)
#example programs for arithmetic operators
a=15
b=4
print("Addition:",a+b)
print("Subtraction:",a-b)
print("Multiplication:",a*b)
print("Division:",a/b)
print("Floor Division:",a//b)
print("Modulus:",a%b)
print("Exponent:",a**b)
#program to find the perimeter of rectangle
l=float(input("Enter the length of rectangle:"))
b=float(input("Enter the breadth of rectangle:"))
perimeter=2*(l+b)
print("Perimeter of rectangle is :",perimeter)
#program to find the area of triangle
base=float(input("Enter the base of triangle:"))
height=float(input("Enter the height of triangle:"))
area_of_triangle=0.5*base*height
print("Area of triangle is :",area_of_triangle)
#program to find the simple interest
p=float(input("Enter the principal amount:"))
r=float(input("Enter the rate of interest:"))
t=float(input("Enter the time in years:"))
simple_interest=(p*r*t)/100
print("Simple Interest is :",simple_interest)
#program to find the compound interest
p=float(input("Enter the principal amount:"))
r=float(input("Enter the rate of interest:"))
t=float(input("Enter the time in years:"))
compound_interest=p*((1+(r/100))**t)-p
print("Compound Interest is :",compound_interest)
#program to convert temperature from celsius to fahrenheit
celsius=float(input("Enter temperature in celsius:"))
fahrenheit=(celsius*9/5)+32
print("Temperature in fahrenheit is :",fahrenheit)
#program to convert distance from kilometers to miles
kilometers=float(input("Enter distance in kilometers:"))
miles=kilometers*0.621371
print("Distance in miles is :",miles)
#program to find the area of square
side=float(input("Enter the side length of square:"))
area_of_square=side**2
print("Area of square is :",area_of_square)
#program to find the circumference of circle
r=float(input("Enter the radius of circle:"))
pi=3.14
circumference=2*pi*r
print("Circumference of circle is :",circumference)
#program to find the volume of cube
side=float(input("Enter the side length of cube:"))
volume_of_cube=side**3
print("Volume of cube is :",volume_of_cube)
#program to find the volume of cylinder
radius=float(input("Enter the radius of cylinder:"))
height=float(input("Enter the height of cylinder:"))
pi=3.14
volume_of_cylinder=pi*(radius**2)*height
print("Volume of cylinder is :",volume_of_cylinder)
#program to find the average of three numbers
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
num3=float(input("Enter third number:"))
average=(num1+num2+num3)/3
print("Average of three numbers is :",average)
#program to find the power of a number
base=float(input("Enter the base number:"))
exponent=float(input("Enter the exponent:"))
power=base**exponent
print("Power of the number is :",power)
#program to find the remainder when one number is divided by another
dividend=int(input("Enter the dividend:"))
divisor=int(input("Enter the divisor:"))
remainder=dividend%divisor
print("Remainder is :",remainder)
#program to find the quotient when one number is divided by another
dividend=int(input("Enter the dividend:"))
divisor=int(input("Enter the divisor:"))
quotient=dividend//divisor
print("Quotient is :",quotient)
#program to find the sum of first n natural numbers
n=int(input("Enter a natural number:"))
sum_of_natural_numbers=n*(n+1)//2
print("Sum of first",n,"natural numbers is :",sum_of_natural_numbers)
#program to find the area of rectangle
length=float(input("Enter the length of rectangle:"))
breadth=float(input("Enter the breadth of rectangle:"))
area_of_rectangle=length*breadth
print("Area of rectangle is :",area_of_rectangle)
#program to find the perimeter of square
side=float(input("Enter the side length of square:"))
perimeter_of_square=4*side
print("Perimeter of square is :",perimeter_of_square)
#program to find the volume of sphere
radius=float(input("Enter the radius of sphere:"))
pi=3.14
volume_of_sphere=(4/3)*pi*(radius**3)
print("Volume of sphere is :",volume_of_sphere)
#program to find the area of parallelogram
base=float(input("Enter the base of parallelogram:"))
height=float(input("Enter the height of parallelogram:"))
area_of_parallelogram=base*height
print("Area of parallelogram is :",area_of_parallelogram)
#program to find the surface area of cube
side=float(input("Enter the side length of cube:"))
surface_area_of_cube=6*(side**2)
print("Surface area of cube is :",surface_area_of_cube)
#program to find the surface area of cylinder
radius=float(input("Enter the radius of cylinder:"))
height=float(input("Enter the height of cylinder:"))
pi=3.14
surface_area_of_cylinder=2*pi*radius*(radius+height)
print("Surface area of cylinder is :",surface_area_of_cylinder)
#program to find the area of trapezium
a=float(input("Enter the length of first parallel side:"))
b=float(input("Enter the length of second parallel side:"))
h=float(input("Enter the height of trapezium:"))
area_of_trapezium=0.5*(a+b)*h
print("Area of trapezium is :",area_of_trapezium)