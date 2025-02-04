# DO NOT using random in production code with security objectives
import random

random_float = random.random()
print(f"Random float between 0.0 and 1.0: {random_float}")

random_int = random.randint(1, 10)
print(f"Random integer between 1 and 10: {random_int}")

elements = ['apple', 'banana', 'cherry', 'date']
random_element = random.choice(elements) # non-empty sequence
print(f"Random element from the list: {random_element}")

elements = ['apple', 'banana', 'cherry', 'date']
random.shuffle(elements) # Shuffles the elements of a list in place
print(f"Shuffled list: {elements}")

elements = ['apple', 'banana', 'cherry', 'date']
sampled_elements = random.sample(elements, 2)
print(f"Random sample of 2 elements from the list: {sampled_elements}")