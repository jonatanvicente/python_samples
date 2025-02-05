# Python 3.10+ example
day = "Monday"

match day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        day_type = "Weekday"
    case "Saturday" | "Sunday":
        day_type = "Weekend"
    case _:
        day_type = "Invalid day"

print(day_type)  # Output: Weekday