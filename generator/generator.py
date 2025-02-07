'''
A generator in Python is a function that uses the yield keyword to return a sequence of values one at a time,
allowing you to iterate over them without storing the entire sequence in memory.
Here is a simple example of a generator that yields the first n Fibonacci numbers:
'''
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a   # returns each Fibonacci number one at a time
        a, b = b, a + b

# Example usage
for number in fibonacci(10):
    print(number)