# String functions examples

# Initializing a string
my_string = "Hello, World!"
'''
 strings are immutable. This means that once a string is created, it cannot be changed. 
 Any operation that modifies a string will create a new string instead of modifying the original one.
Attempting to change a character in the string (this will raise an error)
'''
try:
    my_string[0] = "h"
except TypeError as e:
    print(e)  # Output: 'str' object does not support item assignment

'''
String properties:
    - immutable
    - concatenable
    - multiplicable
    - multiline (double quotes or tripled quotes)
    - indexable
    - contents are iterable and verifiable
'''

# ~~ Methods
# 1. Uppercase
upper_string = my_string.upper()
print(upper_string)  # Output: "HELLO, WORLD!"

# 2. Lowercase
lower_string = my_string.lower()
print(lower_string)  # Output: "hello, world!"

# 3. Capitalize
capitalized_string = my_string.capitalize()
print(capitalized_string)  # Output: "Hello, world!"

# 4. Title
title_string = my_string.title()
print(title_string)  # Output: "Hello, World!"

# 5. Strip (removes leading and trailing whitespace)
stripped_string = "   Hello, World!   ".strip()
print(stripped_string)  # Output: "Hello, World!"

# 6. Replace
replaced_string = my_string.replace("World", "Python")
print(replaced_string)  # Output: "Hello, Python!"

# 7. Split
split_string = my_string.split(", ")
print(split_string)  # Output: ["Hello", "World!"]

# 8. Join
joined_string = ", ".join(["Hello", "Python"])
print(joined_string)  # Output: "Hello, Python"

# 9. Find
index = my_string.find("World")
print(index)  # Output: 7

# 10. Count
count = my_string.count("l")
print(count)  # Output: 3

# 11. Startswith
starts_with = my_string.startswith("Hello")
print(starts_with)  # Output: True

# 12. Endswith
ends_with = my_string.endswith("!")
print(ends_with)  # Output: True

# 13. Format
formatted_string = "My name is {name} and I am {age} years old.".format(name="Alice", age=30)
print(formatted_string)  # Output: "My name is Alice and I am 30 years old."

# 14. F-strings (formatted string literals)
name = "Alice"
age = 30
f_string = f"My name is {name} and I am {age} years old."
print(f_string)  # Output: "My name is Alice and I am 30 years old."

#  index uses

# Initializing a string
my_string = "Hello, World!"

# 1. Finding the index of a substring
index = my_string.index("World")
print(index)  # Output: 7

# 2. Finding the index of a character
index = my_string.index("o")
print(index)  # Output: 4

# 3. Finding the index of a substring starting from a specific position
index = my_string.index("o", 5)
print(index)  # Output: 8

# 4. Finding the index of a substring within a specific range
index = my_string.index("o", 5, 10)
print(index)  # Output: 8

# 5. Handling ValueError when the substring is not found
try:
    index = my_string.index("Python")
except ValueError:
    print("Substring not found")  # Output: Substring not found


# Initializing a string
my_string = "Hello, World!"

# 1. Accessing the last character
last_char = my_string[-1]
print(last_char)  # Output: "!"

# 2. Accessing the second to last character
second_last_char = my_string[-2]
print(second_last_char)  # Output: "d"

# 3. Slicing the last 5 characters
last_five_chars = my_string[-5:]
print(last_five_chars)  # Output: "orld!"

# 4. Slicing the string except the last character
all_but_last = my_string[:-1]
print(all_but_last)  # Output: "Hello, World"

# 5. Slicing a substring using negative indices
substring = my_string[-6:-1]
print(substring)  # Output: "World"