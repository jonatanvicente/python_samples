from datetime import datetime

# Get the current date and time
now = datetime.now()
print("Current date and time:", now)
# Get the current date and time
now = datetime.now()
# Format the date and time
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date and time:", formatted_date)
# Define a date string
date_string = "2023-10-25 14:30:00"
# Parse the date string into a datetime object
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Parsed date and time:", parsed_date)
# Define two dates
date1 = datetime(2023, 10, 25)
date2 = datetime(2023, 11, 5)
# Calculate the difference between the two dates
difference = date2 - date1
print("Difference between dates:", difference)
print("Days between dates:", difference.days)

