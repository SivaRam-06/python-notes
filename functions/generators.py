"""
GENERATORS IN PYTHON – BEGINNER FRIENDLY GUIDE
---------------------------------------------

A generator is a special type of iterator that:
✔ Produces values one at a time
✔ Does NOT store all values in memory
✔ Uses the `yield` keyword instead of `return`

This makes generators:
✅ Memory efficient
✅ Fast for large data
✅ Lazy (values are created only when needed)

-------------------------------------------------------------
1️⃣ NORMAL FUNCTION vs GENERATOR FUNCTION
-------------------------------------------------------------
"""

def normal_function():
    return 1

def generator_function():
    yield 1   # pause here and send value back


print("Normal function call:")
print(normal_function())      # gives value directly

print("\nGenerator function call:")
gen = generator_function()
print(gen)                    # this does NOT run the function

print(next(gen))              # function runs now until first yield


"""
-------------------------------------------------------------
2️⃣ SIMPLE GENERATOR – STEP BY STEP EXECUTION
-------------------------------------------------------------
"""

def simple_generator():
    print("Step 1")
    yield 1

    print("Step 2")
    yield 2

    print("Step 3")
    yield 3


print("\nSimple generator execution:")
g = simple_generator()

print(next(g))   # runs till first yield
print(next(g))   # resumes from previous pause
print(next(g))   # resumes again

# next(g)  → would cause StopIteration


"""
-------------------------------------------------------------
3️⃣ USING GENERATOR IN A FOR LOOP
(for loop automatically handles StopIteration)
-------------------------------------------------------------
"""

print("\nUsing generator in for loop:")
for value in simple_generator():
    print("Received:", value)


"""
-------------------------------------------------------------
4️⃣ PRACTICAL EXAMPLE – SQUARE NUMBERS
-------------------------------------------------------------
"""

def squares(n):
    for i in range(1, n + 1):
        yield i * i


print("\nSquares using generator:")
for num in squares(5):
    print(num)


"""
WHY NOT USE A LIST?

List → stores all values in memory
Generator → gives one value at a time

This is useful for large data.
"""


"""
-------------------------------------------------------------
5️⃣ GENERATOR EXPRESSION (SHORT FORM)
-------------------------------------------------------------
"""

print("\nGenerator expression example:")

cubes = (i ** 3 for i in range(1, 5))

for cube in cubes:
    print(cube)


"""
-------------------------------------------------------------
6️⃣ STOPITERATION (WHEN GENERATOR ENDS)
-------------------------------------------------------------
"""

def count_up_to(n):
    for i in range(1, n + 1):
        yield i
    print("Generator finished")


print("\nManual next() with StopIteration:")

c = count_up_to(3)

try:
    while True:
        print(next(c))
except StopIteration:
    print("No more values")


"""
-------------------------------------------------------------
7️⃣ send() – SENDING VALUE INTO GENERATOR
IMPORTANT:
You must start generator using next() before send()
-------------------------------------------------------------
"""

def echo():
    while True:
        data = yield
        print("You sent:", data)


print("\nUsing send():")

e = echo()
next(e)            # start generator
e.send("Hello")
e.send("Python")


"""
-------------------------------------------------------------
8️⃣ throw() – RAISING EXCEPTION INSIDE GENERATOR
-------------------------------------------------------------
"""

def error_handler():
    while True:
        try:
            value = yield
            print("Received:", value)
        except ValueError:
            print("ValueError caught inside generator")


print("\nUsing throw():")

er = error_handler()
next(er)

er.send("Good")
er.throw(ValueError)
er.send("Still running")


"""
-------------------------------------------------------------
9️⃣ close() – STOP A GENERATOR
-------------------------------------------------------------
"""

def count_forever():
    i = 1
    while True:
        yield i
        i += 1


print("\nUsing close():")

cf = count_forever()

print(next(cf))
print(next(cf))

cf.close()

try:
    next(cf)
except StopIteration:
    print("Generator closed")


"""
-------------------------------------------------------------
🔟 yield from  → COMBINING GENERATORS
-------------------------------------------------------------
"""

def gen_a():
    yield "A1"
    yield "A2"

def gen_b():
    yield "B1"
    yield "B2"

def combined():
    yield from gen_a()
    yield from gen_b()


print("\nUsing yield from:")

for item in combined():
    print(item)


"""
-------------------------------------------------------------
⭐ REAL LIFE USE CASE – READING LARGE FILE
-------------------------------------------------------------
"""

def read_lines():
    for i in range(1, 4):
        yield f"Line {i}"


print("\nReading data lazily:")

for line in read_lines():
    print(line)


"""
-------------------------------------------------------------
🎯 SUMMARY
-------------------------------------------------------------

Generator:
✔ Uses yield
✔ Returns values one at a time
✔ Memory efficient
✔ Can pause and resume

Important functions:
next()   → get next value
send()   → send value into generator
throw()  → raise exception inside generator
close()  → stop generator
yield from → combine generators
"""