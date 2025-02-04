
# enumerate is used to access to an index in a collection

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
# Output:
# 0 apple
# 1 banana
# 2 cherry

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
# Output:
# 1 apple
# 2 banana
# 3 cherry

points = [(1, 2), (3, 4), (5, 6)]
for index, (x, y) in enumerate(points):
    print(f"Point {index}: x={x}, y={y}")
# Output:
# Point 0: x=1, y=2
# Point 1: x=3, y=4
# Point 2: x=5, y=6

word = "hello"
for index, char in enumerate(word):
    print(index, char)
# Output:
# 0 h
# 1 e
# 2 l
# 3 l
# 4 o