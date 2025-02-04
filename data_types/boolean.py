# Initializing boolean variables
bool_true = True
bool_false = False

# 1. Logical AND
and_result = bool_true and bool_false
print(and_result)  # Output: False

# 2. Logical OR
or_result = bool_true or bool_false
print(or_result)  # Output: True

# 3. Logical NOT
not_result = not bool_true
print(not_result)  # Output: False

# 4. Equality check
equality_result = (bool_true == bool_false)
print(equality_result)  # Output: False

# 5. Inequality check
inequality_result = (bool_true != bool_false)
print(inequality_result)  # Output: True

# 6. Boolean conversion from integer
bool_from_int = bool(1)  # Non-zero integers are True
print(bool_from_int)  # Output: True

# 7. Boolean conversion from string
bool_from_str = bool("False")  # Non-empty strings are True
print(bool_from_str)  # Output: True

# 8. Boolean conversion from list
bool_from_list = bool([])  # Empty lists are False
print(bool_from_list)  # Output: False

# 9. Boolean conversion from None
bool_from_none = bool(None)  # None is False
print(bool_from_none)  # Output: False

# 10. Using booleans in conditional statements
if bool_true:
    print("This is True")  # Output: This is True
else:
    print("This is False")