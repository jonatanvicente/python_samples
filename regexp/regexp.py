import re

# Matching a pattern
# Check if the string starts with 'Hello'
pattern = r'^Hello'
string = 'Hello, world!'
match = re.match(pattern, string)
if match:
    print("Match found:", match.group())
else:
    print("No match")

# Searching for a pattern
# Search for the first occurrence of 'world' in the string
pattern = r'world'
string = 'Hello, world!'
search = re.search(pattern, string)
if search:
    print("Search found:", search.group())
else:
    print("No match")

# Finding all matches
# Find all occurrences of 'world' in the string
pattern = r'world'
string = 'world Hello, world!'
matches = re.findall(pattern, string)
print("All matches:", matches)

# Replacing a pattern
# Replace 'world' with 'Python' in the string
pattern = r'world'
replacement = 'Python'
string = 'Hello, world!'
new_string = re.sub(pattern, replacement, string)
print("Replaced string:", new_string)

# Splitting a string by a pattern
# Split the string by commas
pattern = r',\s*'
string = 'apple, banana, cherry'
split_list = re.split(pattern, string)
print("Split list:", split_list)