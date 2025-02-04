

cities_population = {"Tijuana":1810645, "León":1579803}
list_values = [5**5, 12**2, 3050, 475*2]

print(min(cities_population.keys()))
print(max(cities_population.values()))
print(max(list_values))

numbers = [10, 20, 5, 40, 15]
min_number = min(numbers)
max_number = max(numbers)
print(f"The smallest number is {min_number}")
print(f"The largest number is {max_number}")

# used to find the lexicographically smallest and largest strings in a list of words
words = ["apple", "banana", "cherry", "date"]
min_word = min(words)
max_word = max(words)
print(f"The lexicographically smallest word is '{min_word}'")
print(f"The lexicographically largest word is '{max_word}'")