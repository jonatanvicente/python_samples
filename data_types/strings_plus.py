# Initializing a string
my_string = "Hello, World!"

# 1. capitalize
print(my_string.capitalize())  # Output: "Hello, world!"

# 2. casefold
print(my_string.casefold())  # Output: "hello, world!"

# 3. center
print(my_string.center(20, '*'))  # Output: "***Hello, World!***"

# 4. count
print(my_string.count('l'))  # Output: 3

# 5. encode
print(my_string.encode())  # Output: b'Hello, World!'

# 6. endswith
print(my_string.endswith('!'))  # Output: True

# 7. expandtabs
print("Hello\tWorld".expandtabs(4))  # Output: "Hello   World"

# 8. find
print(my_string.find('World'))  # Output: 7

# 9. format
print("My name is {name}".format(name="Alice"))  # Output: "My name is Alice"

# 10. format_map
print("{x} {y}".format_map({'x': 'Hello', 'y': 'World'}))  # Output: "Hello World"

# 11. index
print(my_string.index('World'))  # Output: 7

# 12. isalnum
print(my_string.isalnum())  # Output: False

# 13. isalpha
print(my_string.isalpha())  # Output: False

# 14. isascii
print(my_string.isascii())  # Output: True

# 15. isdecimal
print(my_string.isdecimal())  # Output: False

# 16. isdigit
print(my_string.isdigit())  # Output: False

# 17. isidentifier
print(my_string.isidentifier())  # Output: False

# 18. islower
print(my_string.islower())  # Output: False

# 19. isnumeric
print(my_string.isnumeric())  # Output: False

# 20. isprintable
print(my_string.isprintable())  # Output: True

# 21. isspace
print(my_string.isspace())  # Output: False

# 22. istitle
print(my_string.istitle())  # Output: False

# 23. isupper
print(my_string.isupper())  # Output: False

# 24. join
print(", ".join(['Hello', 'World']))  # Output: "Hello, World"

# 25. ljust
print(my_string.ljust(20, '*'))  # Output: "Hello, World!*******"

# 26. lower
print(my_string.lower())  # Output: "hello, world!"

# 27. lstrip
print("   Hello, World!   ".lstrip())  # Output: "Hello, World!   "

# 28. maketrans and translate
trans = str.maketrans("H", "J")
print(my_string.translate(trans))  # Output: "Jello, World!"

# 29. partition
print(my_string.partition(','))  # Output: ('Hello', ',', ' World!')

# 30. replace
print(my_string.replace('World', 'Python'))  # Output: "Hello, Python!"

# 31. rfind
print(my_string.rfind('l'))  # Output: 9

# 32. rindex
print(my_string.rindex('l'))  # Output: 9

# 33. rjust
print(my_string.rjust(20, '*'))  # Output: "*******Hello, World!"

# 34. rpartition
print(my_string.rpartition(','))  # Output: ('Hello', ',', ' World!')

# 35. rsplit
print(my_string.rsplit(', '))  # Output: ['Hello', 'World!']

# 36. rstrip
print("   Hello, World!   ".rstrip())  # Output: "   Hello, World!"

# 37. split
print(my_string.split(', '))  # Output: ['Hello', 'World!']

# 38. splitlines
print("Hello\nWorld".splitlines())  # Output: ['Hello', 'World']

# 39. startswith
print(my_string.startswith('Hello'))  # Output: True

# 40. strip
print("   Hello, World!   ".strip())  # Output: "Hello, World!"

# 41. swapcase
print(my_string.swapcase())  # Output: "hELLO, wORLD!"

# 42. title
print(my_string.title())  # Output: "Hello, World!"

# 43. upper
print(my_string.upper())  # Output: "HELLO, WORLD!"

# 44. zfill
print("42".zfill(5))  # Output: "00042"


# slicing
# Initializing a string
my_string = "Hello, World!"

# 1. Slicing a substring from index 0 to 4
substring = my_string[0:5]
print(substring)  # Output: "Hello"

# 2. Slicing a substring from index 7 to the end
substring = my_string[7:]
print(substring)  # Output: "World!"

# 3. Slicing a substring from the beginning to index 4
substring = my_string[:5]
print(substring)  # Output: "Hello"

# 4. Slicing the entire string
substring = my_string[:]
print(substring)  # Output: "Hello, World!"

# 5. Slicing with a step
substring = my_string[::2]
print(substring)  # Output: "Hlo ol!"

# 6. Slicing with negative indices
substring = my_string[-6:-1]
print(substring)  # Output: "World"