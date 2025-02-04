
# Arithmethic operators
# Addition
result = 10 + 5  # Output: 15
print(result)
# Subtraction
result = 10 - 5  # Output: 5
print(result)
# Multiplication
result = 10 * 5  # Output: 50
print(result)
# Division
result = 10 / 5  # Output: 2.0
print(result)
# Floor Division
result = 10 // 3  # Output: 3
print(result)
# Modulus
result = 10 % 3  # Output: 1
print(result)
# Exponentiation
result = 2 ** 3  # Output: 8
print(result)

# Comparison operators
# Equal
result = (10 == 5)  # Output: False
print(result)
# Not Equal
result = (10 != 5)  # Output: True
print(result)
# Greater Than
result = (10 > 5)  # Output: True
print(result)
# Less Than
result = (10 < 5)  # Output: False
print(result)
# Greater Than or Equal To
result = (10 >= 5)  # Output: True
print(result)
# Less Than or Equal To
result = (10 <= 5)  # Output: False
print(result)

# Logical operators
# And
result = (10 > 5 and 10 < 20)  # Output: True
print(result)
# Or
result = (10 > 5 or 10 > 20)  # Output: True
print(result)
# Not
result = not(10 > 5)  # Output: False
print(result)

# Bitwise operators
# AND
result = 10 & 5  # Output: 0
print(result)
# OR
result = 10 | 5  # Output: 15
print(result)
# XOR
result = 10 ^ 5  # Output: 15
print(result)
# NOT
result = ~10  # Output: -11
print(result)
# Left Shift
result = 10 << 2  # Output: 40
print(result)
# Right Shift
result = 10 >> 2  # Output: 2
print(result)

# Assignment operators
# Assign
x = 10
print(x)
# Add and Assign
x += 5  # x is now 15
print(x)
# Subtract and Assign
x -= 5  # x is now 10
print(x)
# Multiply and Assign
x *= 5  # x is now 50
print(x)
# Divide and Assign
x /= 5  # x is now 10.0
print(x)
# Floor Divide and Assign
x //= 3  # x is now 3.0
print(x)
# Modulus and Assign
x %= 3  # x is now 0.0
print(x)
# Exponentiate and Assign
x **= 3  # x is now 0.0
print(x)
# Bitwise AND and Assign
x = 1 #avoiding 0
x &= 5
print(x)
# Bitwise OR and Assign
x |= 5  # x is now 5
print(x)
# Bitwise XOR and Assign
x ^= 5  # x is now 0
print(x)
# Bitwise Left Shift and Assign
x <<= 2  # x is now 0
print(x)
# Bitwise Right Shift and Assign
x >>= 2  # x is now 0
print(x)

# Membership operators
# In
result = 5 in [1, 2, 3, 4, 5]  # Output: True
print(result)
# Not In
result = 6 not in [1, 2, 3, 4, 5]  # Output: True
print(result)

# Identity operators
# Is
x = [1, 2, 3]
y = x
result = (x is y)  # Output: True
print(result)
# Is Not
y = [1, 2, 3]
result = (x is not y)  # Output: True
print(result)


# Rounding
print(round(100/3))
print(round(12/7,2))