print('hola pp');
print(500+55);
print('Your name is ' + input('Name: '));

# data types
my_int = 10
my_float = 10.5
my_string = "Hello, World!"
my_bool = True
my_list = [1, 2, 3, 4, 5] #mutable
# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
# Attempting to modify an element will result in an error
# my_tuple[0] = 10  # This will raise a TypeError
# You can, however, create a new tuple by concatenation
new_tuple = my_tuple + (6, 7) #immutable
print(new_tuple)  # Output: (1, 2, 3, 4, 5, 6, 7)

# Creating a set - mutable
my_set = {1, 2, 3, 4, 5}
# Adding an element to the set
my_set.add(6)
# Removing an element from the set
my_set.remove(3)
# Checking if an element is in the set
print(4 in my_set)  # Output: True
# Iterating over a set
for element in my_set:
    print(element)
# Output the set
print(my_set)  # Output: {1, 2, 4, 5, 6}

# Dictionary
my_dict = {"name": "John", "age": 30} #mutable
# NoneType
my_none = None