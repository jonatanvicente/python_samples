# For loop
# Example 1
for i in range(5):
    print(i)  # Output: 0 1 2 3 4

# Example 2
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # Output: apple banana cherry

    # While loop
    # Example 1
    count = 0
    while count < 5:
        print(count)
        count += 1  # Output: 0 1 2 3 4

    # Example 2
    num = 10
    while num > 0:
        print(num)
        num -= 2  # Output: 10 8 6 4 2

# Break sentence
# Example 1
for i in range(10):
    if i == 5:
        break
    print(i)  # Output: 0 1 2 3 4

# Example 2
count = 0
while count < 10:
    if count == 7:
        break
    print(count)
    count += 1  # Output: 0 1 2 3 4 5 6


    # Continue sentence

    # Example 1
    for i in range(10):
        if i % 2 == 0:
            continue
        print(i)  # Output: 1 3 5 7 9

    # Example 2
    count = 0
    while count < 10:
        count += 1
        if count % 2 == 0:
            continue
        print(count)  # Output: 1 3 5 7 9


        #Pass sentence

        # Example 1
        for i in range(5):
            pass  # No operation


        # Example 2
        def my_function():
            pass  # No operation