# Zipping two lists

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

combined = zip(names, ages)

# The function stops when the iterable with the fewest elements is exhausted
for name, age in combined:
    print(f"{name} is {age} years old")


# Unzipping a list of tuples
combined = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]

names, ages = zip(*combined)

print("Names:", names)
print("Ages:", ages)