# Integer to float
my_int = 10
my_float = float(my_int)
print(my_float)  # Output: 10.0

# Float to integer
my_float = 10.5
my_int = int(my_float)
print(my_int)  # Output: 10

# Integer to string
my_int = 10
my_string = str(my_int)
print(my_string)  # Output: "10"

# String to integer
my_string = "10"
my_int = int(my_string)
print(my_int)  # Output: 10

# String to float
my_string = "10.5"
my_float = float(my_string)
print(my_float)  # Output: 10.5

# List to tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3)

# Tuple to list
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)  # Output: [1, 2, 3]

# Set to list
my_set = {1, 2, 3}
my_list = list(my_set)
print(my_list)  # Output: [1, 2, 3]

# List to set
my_list = [1, 2, 3, 3]
my_set = set(my_list)
print(my_set)  # Output: {1, 2, 3}

# type
num1 = 7
print(type(num1))

#cast, truncate
print (int(7.5))

print('My car is {} and its number is {}'.format('Toyota', 1234));

def greet(name, age):
    return f"Hello, {name}! You are {age} years old."

# Example usage
name = "Alice"
age = 30
print(greet(name, age))  # Output: Hello, Alice! You are 30 years old.