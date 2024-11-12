# Constants
SECONDS_IN_A_MINUTE = 60
SECONDS_IN_A_HOUR = 3600
SECONDS_IN_A_DAY = 86400

total_seconds = int(input("Enter the number of seconds: "))

days = total_seconds // SECONDS_IN_A_DAY
remaining_seconds = total_seconds % SECONDS_IN_A_DAY

hours = remaining_seconds // SECONDS_IN_A_HOUR
remaining_seconds %= SECONDS_IN_A_HOUR

minutes = remaining_seconds // SECONDS_IN_A_MINUTE
remaining_seconds %= SECONDS_IN_A_MINUTE

seconds = remaining_seconds

print(f"{total_seconds} seconds are equal to:")
print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")