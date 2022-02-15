# # Data Types

# String

"Hello"[4]

# Subscripting is pulling out parts of a string

# print("123" + "345")  # cocatinates


# Integer - whole numbers, no decimals

# print(123 + 345)

123_456_789

# Float - has decimal place(s)

# Boolean - only two values, True or False

True

False

# # Type Error, Type Checking and Type Conversion

# num_char = len(input("What is your name?"))
# type()  # check type of variable and returns its type

# type conversion or also known as type casting

# new_num_char = str(num_char)

# print("Your name has " + new_num_char + " characters.")

a = float(123)
print(type(a))


# Mathematical Operations

3 + 5

7 - 4

3 * 2

6 / 3  # always a float

2 ** 3  # get the exponent of 2 to the power of 3

# be careful of order of operations
# PEMDASLR
# ()
# **
# * /
# + -

# Number Manipulation and F Strings in Python

# print(round(8 / 3, 2)) # round(args, decimal place)

print(8 // 3)  # floor type is integer

result = 4 / 2
result /= 2
print(result)

score = 0
height = 1.85
isWinning = True
# User scores a point
score += 1
print("your score is " + str(score))

# f-string

print(
    f"your score is {score}, your height is {height}, your are winning is {isWinning}")
