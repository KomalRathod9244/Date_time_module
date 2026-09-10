import datetime
from datetime import datetime
from datetime import date
from datetime import timedelta
import calendar


# 1.Take a year, a month, and a day number and find out on which date that day falls.

y = int(input("Enter the year : "))
m = int(input("Enter the month : "))
d = int(input("Enter the day : "))
date_ = datetime.date(y,m,d)
print("User entered date : ",date_)


weekday_n = datetime.datetime.weekday(date_)

def day_name(weekday_n):
    weekday_ = ''
    if weekday_n == 0:
        weekday_ = 'Monday'
    elif weekday_n == 1:
        weekday_ = 'Tuesday'
    elif weekday_n == 2:
        weekday_ = 'Wednesday'
    elif weekday_n == 3:
        weekday_ = 'Thursday'
    elif weekday_n == 4:
        weekday_ = 'Friday'
    elif weekday_n == 5:
        weekday_ = 'Saturday'
    elif weekday_n == 6:
        weekday_ = 'Sunday'
        
    return weekday_

# 2.  Take a year from the user and determine if it's a leap year. If it is a leap year, find out which day the twenty-ninth of February falls on.
y = int(input("Enter year : "))
leap = False
if y % 4 == 0:
    if y % 100 == 0:
        y //= 100

        if y % 4 == 0:
            leap = True
        else:
            leap = False
    else:
        leap = True

if leap:
    print(f"{y} is a leap year")
else:
    print(f"{y} is not a leap year ")

if leap:
    leap_year_date = datetime.date(y, 2, 29)
    print("Date at 29th of Feb : ",leap_year_date)
    date_feb_twenty_nine = datetime.datetime.weekday(leap_year_date)
    print(day_name(date_feb_twenty_nine))


# 3.  Take a date of birth (DOB) from the user and calculate and print their age in year, month, and day format.

# DOB = 15-06-2003
# Today = 10-09-2026

dob_input = input("Enter DOB (DD-MM-YYYY): ")

try:
    day, month, year = map(int, dob_input.split("-"))
    dob = date(year, month, day)
    today = date.today()

    if dob > today:
        raise ValueError("DOB cannot be in the future.")

    age_years = today.year - dob.year
    age_months = today.month - dob.month
    age_days = today.day - dob.day

    if age_days < 0:
        age_months -= 1

        previous_month = today.month - 1
        previous_year = today.year

        if previous_month == 0:
            previous_month = 12
            previous_year -= 1

        age_days += calendar.monthrange(previous_year, previous_month)[1]

    if age_months < 0:
        age_years -= 1
        age_months += 12

    print(f"Age: {age_years} years, {age_months} months, {age_days} days")

except ValueError as e:
    print(f"Invalid input: {e}")

# 4.  Print a message based on the current time:

#   If the current time is between 4 AM and 12 PM, the message should be "Good morning."
#   If the current time is between 12 PM and 4 PM, the message should be "Good afternoon."
#   If the current time is between 4 PM and 7 PM, the message should be "Good evening."
#   If the current time is between 7 PM and 4 AM, the message should be "Good night."



current_time = datetime.now()
print(f"{current_time} = datetime.now() ")
hour = current_time.hour

if 4 <= hour < 12:
    print("Good morning.")

elif 12 <= hour < 16:
    print("Good afternoon.")

elif 16 <= hour < 19:
    print("Good evening.")

else:
    print("Good night.")



# 5.  Take a year from the user and determine how many times Monday, Tuesday, Wednesday, and Thursday occur separately in that year. Also, determine the occurrences of weeks, weekdays, and weekends in that year.


year = int(input("Enter year: "))

start_date = date(year, 1, 1)
# print(f"{start_date} = date(year, 1, 1)")
end_date = date(year + 1, 1, 1)
# print(f"{end_date} = date(year + 1, 1, 1)")

monday = 0
tuesday = 0
wednesday = 0
thursday = 0

weekdays = 0
weekends = 0
total_days = 0

current_date = start_date

while current_date < end_date:

    # Monday = 0, Tuesday = 1, ..., Sunday = 6
    day = current_date.weekday()

    if day == 0:
        monday += 1
    elif day == 1:
        tuesday += 1
    elif day == 2:
        wednesday += 1
    elif day == 3:
        thursday += 1

    # Weekdays = Monday to Friday
    if day < 5:
        weekdays += 1
    else:
        weekends += 1

    total_days += 1
    current_date += timedelta(days=1)
# print(f"{current_date} = timedelta(days=1)")
# print(f"{current_date+timedelta(days=1)} = timedelta(days=1)")

print("\n===== Year Statistics =====")
print(f"Monday    : {monday}")
print(f"Tuesday   : {tuesday}")
print(f"Wednesday : {wednesday}")
print(f"Thursday  : {thursday}")

print(f"\nTotal days : {total_days}")
print(f"Weekdays   : {weekdays}")
print(f"Weekends   : {weekends}")
print(f"Weeks      : {total_days / 7:.2f}")



# 6.  Take a string from the user in the format "August,29, 2025, 02:20 PM," and convert it to the format "2025-08-29 14:20:00."


user_input = input("Enter date and time in the format 'August,29, 2025, 02:20 PM,': ")

try:
    date_time = datetime.strptime(
        user_input.strip(),
        "%B,%d, %Y, %I:%M %p,"
    )
    # print(f'{date_time} = datetime.strptime(user_input.strip(), "%B,%d, %Y, %I:%M %p,")')

    result = date_time.strftime("%Y-%m-%d %H:%M:%S")
    # print(f'{result} = date_time.strftime("%Y-%m-%d %H:%M:%S")')
    print("Converted date and time:", result)

except ValueError:
    print("Invalid date/time format.")



# 7  Take the number of days from the user and print the date that comes after those many days from the current date, and the date that comes before those many days from the current date. If either of those dates falls on a Saturday or Sunday, print the message "Hurry!"; otherwise, print the message "Oh."


days = int(input("Enter number of days: "))

today = date.today ()

after_date = today + timedelta(days=days)
before_date = today - timedelta(days=days)
# print("timedelta(days=days) = ",timedelta(days=days))
print("Current Date :", today)
print("After", days, "days :", after_date)
print("Before", days, "days:", before_date)

# Saturday = 5, Sunday = 6
if after_date.weekday() >= 5 or before_date.weekday() >= 5:
    print("Hurry!")
else:
    print("Oh.")
'''
'''
