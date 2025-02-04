# Initializing a dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# 1. Accessing a value by key
name = my_dict["name"]
print(name)  # Output: John

# 2. Adding a new key-value pair
my_dict["email"] = "john@example.com"
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'email': 'john@example.com'}

# 3. Updating the value of an existing key
my_dict["age"] = 31
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'email': 'john@example.com'}

# 4. Removing a key-value pair using pop
email = my_dict.pop("email")
print(email)  # Output: john@example.com
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York'}

# 5. Removing the last inserted key-value pair using popitem
last_item = my_dict.popitem()
print(last_item)  # Output: ('city', 'New York')
print(my_dict)  # Output: {'name': 'John', 'age': 31}

# 6. Getting a value by key using get
age = my_dict.get("age")
print(age)  # Output: 31

# 7. Getting all keys using keys
keys = my_dict.keys()
print(keys)  # Output: dict_keys(['name', 'age'])

# 8. Getting all values using values
values = my_dict.values()
print(values)  # Output: dict_values(['John', 31])

# 9. Getting all key-value pairs using items
items = my_dict.items()
print(items)  # Output: dict_items([('name', 'John'), ('age', 31)])

# 10. Checking if a key exists using in
has_name = "name" in my_dict
print(has_name)  # Output: True

# 11. Clearing all key-value pairs using clear
my_dict.clear()
print(my_dict)  # Output: {}

# Re-initializing the dictionary for further examples
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# 12. Copying a dictionary using copy
copied_dict = my_dict.copy()
print(copied_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# 13. Updating a dictionary with another dictionary using update
my_dict.update({"email": "john@example.com", "age": 31})
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'email': 'john@example.com'}

# 14. Creating a dictionary with default values using fromkeys
keys = ["name", "age", "city"]
default_dict = dict.fromkeys(keys, "unknown")
print(default_dict)  # Output: {'name': 'unknown', 'age': 'unknown', 'city': 'unknown'}