'''
A Python list can contain elements of various data types, including integers, floats, strings, booleans,
lists, tuples, sets, dictionaries, and NoneType
'''

# Initializing a list with various data types
my_list = [
    10,                      # Integer
    10.5,                    # Float
    "Hello, World!",         # String
    True,                    # Boolean
    [1, 2, 3],               # List
    (4, 5, 6),               # Tuple
    {7, 8, 9},               # Set
    {"name": "John", "age": 30},  # Dictionary
    None                     # NoneType
]

# Printing the list
print(my_list)

'''
    List comprehension to create a list of squares
    This code creates a list of squares of numbers from 1 to 10 using list comprehension. The range(1, 11) generates numbers from 1 to 10, and x**2 computes the square of each number.
'''
squares = [x**2 for x in range(1, 11)]

# Printing the list of squares
print(squares)

