# Bitwise operators
'''
-These operators are used to perform bit-level operations on binary numbers.
The bitwise operators are:
    &  - Bitwise AND
    |  - Bitwise OR
    ^  - Bitwise XOR
    ~  - Bitwise NOT
    << - Left Shift
    >> - Right Shift
'''
#bitwise AND (&) operator:
'''
-if both bits are 1, the result is 1; otherwise, the result is 0.
Example:
    a = 5  # Binary: 0101
    b = 3  # Binary: 0011
    result = a & b  # Binary: 0001 (Decimal: 1)
    print(result)  # Output: 1
'''
#bitwise OR (|) operator:
'''
-if at least one bit is 1, the result is 1; otherwise, the result is 0.
Example:
    a = 5  # Binary: 0101
    b = 3  # Binary: 0011
    result = a | b  # Binary: 0111 (Decimal: 7)
    print(result)  # Output: 7
'''
#bitwise XOR (^) operator:
'''
-if the bits are different, the result is 1; otherwise, the result is 0.
Example:
    a = 5  # Binary: 0101
    b = 3  # Binary: 0011
    result = a ^ b  # Binary: 0110 (Decimal: 6)
    print(result)  # Output: 6
'''
#bitwise NOT (~) operator:
'''
-This operator inverts the bits of the operand (0s become 1s and 1s become 0s).
Example:
    a = 5  # Binary: 0101
    result = ~a  # Binary: 1010 (Decimal: -6)
    print(result)  # Output: -6
'''
#left shift (<<) operator:
'''
-This operator shifts the bits of the operand to the left by the specified number of positions,
filling the rightmost bits with 0s.
Example:
    a = 5  # Binary: 0101
    result = a << 2  # Binary: 010100 (Decimal: 20)
    print(result)  # Output: 20
'''
#right shift (>>) operator:
'''
-This operator shifts the bits of the operand to the right by the specified number of positions,
filling the leftmost bits with 0s.
Example:
    a = 20  # Binary: 010100
    result = a >> 2  # Binary: 000101 (Decimal: 5)
    print(result)  # Output: 5
'''
'''
# Example to demonstrate bitwise operators
a = 12  # Binary: 1100
b = 5   # Binary: 0101
print("Bitwise AND (&):", a & b)   # Output: 4 (Binary: 0100)
print("Bitwise OR (|):", a | b)    # Output: 13 (Binary: 1101)
print("Bitwise XOR (^):", a ^ b)   # Output: 9 (Binary: 1001)
print("Bitwise NOT (~) of a:", ~a)  # Output: -13
print("Left Shift (<<) a by 2:", a << 2)  # Output: 48 (Binary: 110000)
print("Right Shift (>>) a by 2:", a >> 2) # Output: 3 (Binary: 0011)
'''
'''
In which scenarios bitwise operators are used?
Bitwise operators are commonly used in scenarios such as:
1. Low-level programming and hardware interfacing
2. Cryptography and data encryption
3. Network programming and IP address manipulation
4. Performance optimization in certain algorithms
5. Graphics programming and image processing
Understanding bitwise operators is essential for tasks that require direct manipulation of binary data.
'''
'''
How to identify the where to use this operator by looking at the problem statement in simple english in the points?
1. Look for keywords like "bits", "binary", "flags", "masks", "low-level operations", or any mention of direct manipulation of binary data.
2. Check if the problem involves manipulating individual bits in a number.
3. Identify if the problem requires implementing efficient algorithms for tasks like finding unique elements, counting set bits, etc.
4. Determine if the problem involves performing operations on flags and masks.
5. Assess whether the problem requires working with binary representations of data.
6. Consider if the problem is about optimizing performance in low-level operations.
Understanding bitwise operators is essential for tasks that require direct manipulation of binary data.
'''
#some programs where bitwise operators are used
'''
#using bitwise operators to solve problems
#offer: buy two get 60% off, buy 1 get 30% off
#input: two lines
#first line: no of products brought
#second line: price of each product assuming all are of equal price
#output: final amount customer has to pay
'''
no_of_products=int(input("Enter no of products: "))
price_per_product=int(input("Enter the price of the product: "))
pairs = no_of_products//2
single = price_per_product%2
total = 0.4*price_per_product*2 + 0.7*single*price_per_product
print(total)
'''
(OR)

no_of_products=int(input("Enter no of products: "))
price_per_product=int(input("Enter the price of the product: "))
if no_of_products==2:
    total_amount=2*price_per_product*0.4
    print("final amount to be paid is :",total_amount)
elif no_of_products==1:
    total_amount=price_per_product*0.7
    print("final amount to be paid is :",total_amount)
else:
    total_amount=no_of_products*price_per_product
    print("final amount to be paid is :",total_amount)
'''
'''
#1. Check if a number is even or odd using bitwise AND operator
num = 7
if num & 1:
    print(num, "is odd")
else:
    print(num, "is even")
#2. Swap two numbers using bitwise XOR operator
x = 10
y = 5
x = x ^ y
y = x ^ y
x = x ^ y
print("After swapping: x =", x, ", y =", y)
#3. Find the maximum of two numbers using bitwise operators
a = 15
b = 10
max_num = a - ((a - b) & ((a - b) >> 31))
print("Maximum number is:", max_num)
#4. Count the number of set bits in an integer using bitwise AND operator
def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
number = 29  # Binary: 11101
print("Number of set bits in", number, "is:", count_set_bits(number))
#5. Clear the least significant bit of a number using bitwise AND operator
num = 14  # Binary: 1110
cleared_num = num & (num - 1)
print("Number after clearing least significant bit:", cleared_num)
#6. Perform left and right shifts on a number
num = 8  # Binary: 1000
left_shifted = num << 2
right_shifted = num >> 2
print("Left shifted by 2:", left_shifted)   # Output: 32 (Binary: 100000)
print("Right shifted by 2:", right_shifted) # Output: 2 (Binary: 10)
#7. Toggle specific bits in a number using bitwise XOR operator
num = 10  # Binary: 1010
mask = 5  # Binary: 0101
toggled_num = num ^ mask
print("Number after toggling bits:", toggled_num)
#8. Check if two numbers have opposite signs using bitwise XOR operator
a = 10
b = -5
if (a ^ b) < 0:
    print("a and b have opposite signs")
else:
    print("a and b have the same sign")
#9. Find the power of two using left shift operator
n = 3
power_of_two = 1 << n
print("2 raised to the power", n, "is:", power_of_two)
#10. Isolate the rightmost set bit of a number using bitwise AND operator
num = 18  # Binary: 10010
rightmost_set_bit = num & -num
print("Rightmost set bit of", num, "is:", rightmost_set_bit)
'''