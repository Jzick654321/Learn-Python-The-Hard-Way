def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b
# subtracting a from b
def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b
# multiplying from a to b
def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b
# dividing a from b
def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

# printing
print("Let's do some math with just functions!")
# giving numbers for a and b
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
# printing
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")
# adding, subtracting, multiplying, and dividing.
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# printing.
print("That becomes: ", what, "Can you do it by hand?")