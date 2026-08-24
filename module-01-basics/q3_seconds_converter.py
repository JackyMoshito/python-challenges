# Number of Seconds
number_of_seconds = int(input("Enter the number of seconds: "))

# Convert seconds
hours = number_of_seconds // 3600
remaining_seconds = number_of_seconds % 3600

# Convert minutes
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"The {number_of_seconds} seconds, is equal to {hours} hour, {minutes} minutes, {seconds} seconds")
