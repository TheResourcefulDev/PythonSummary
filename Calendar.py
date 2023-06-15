import time
import calendar

"""
This is a tutorial on date and time in Python.

Python provides built-in modules such as `time` and `calendar` to work with dates, times, and calendars.

Unix timestamp is a way to represent time as the number of seconds that have elapsed since January 1, 1970 (UTC). A tick is a unit of time measurement in Python, typically representing a fraction of a second.

Time tuple is a tuple that represents time in a structured format. It consists of nine elements: year, month, day, hour, minute, second, weekday, Julian day, and daylight saving flag.

The `struct_time` structure is returned by various time-related functions and represents time values as attributes, making it easy to access different components of a date and time.

The time module provides various functions and attributes for working with time, such as `time()`, `asctime()`, `clock()`, `ctime()`, `gmtime()`, `localtime()`, `mktime()`, `sleep()`, `strftime()`, `strptime()`, `tzset()`, `altzone`, `tzname`, and more.

The calendar module provides functions to work with calendars, such as `calendar()`, `firstweekday()`, `isleap()`, `month()`, `monthcalendar()`, `prcal()`, `prmonth()`, `setfirstweekday()`, `timegm()`, and `weekday()`.
"""

# Getting the current time in seconds (Unix timestamp)
current_time = time.time()
print("Unix timestamp:", current_time)

# Getting the current time in a structured format (time tuple)
time_tuple = time.localtime(current_time)
print("Time tuple:", time_tuple)

# Getting the difference in seconds between local time and UTC (in seconds)
time_difference = time.altzone
print("Time difference:", time_difference)

# Getting a formatted string representation of the time
formatted_time = time.asctime(time_tuple)
print("Formatted time:", formatted_time)

# Getting a string representation of the current local time
local_time_string = time.ctime()
print("Local time string:", local_time_string)

# Getting the current time in UTC (time tuple)
utc_time_tuple = time.gmtime(current_time)
print("UTC time tuple:", utc_time_tuple)

# Getting the current local time (time tuple)
local_time_tuple = time.localtime(current_time)
print("Local time tuple:", local_time_tuple)

# Converting a time tuple to a Unix timestamp
converted_timestamp = time.mktime(time_tuple)
print("Converted timestamp:", converted_timestamp)

# Pausing the program execution for a specified number of seconds
time.sleep(2)
print("Pause for 2 seconds")

# Formatting time as a string
formatted_string = time.strftime("%Y-%m-%d %H:%M:%S", time_tuple)
print("Formatted string:", formatted_string)

# Parsing a string to a time tuple
parsed_time = time.strptime("2023-06-15", "%Y-%m-%d")
print("Parsed time tuple:", parsed_time)

# Getting the current time in seconds
current_time_seconds = time.time()
print("Current time in seconds:", current_time_seconds)

# Setting the time conversion rules#
#time.tzset()
print("Time conversion rules set")

# Getting the time zone name(s)
timezone_names = time.tzname
print("Time zone names:", timezone_names)


# Getting a calendar for the year and month
calendar_month = calendar.month(2023, 6)
print("Calendar for June 2023:")
print(calendar_month)

# Getting the first weekday of the week (0 for Monday, 6 for Sunday)
first_weekday = calendar.firstweekday()
print("First weekday of the week:", first_weekday)

# Checking if a year is a leap year
is_leap_year = calendar.isleap(2024)
print("Is 2024 a leap year?", is_leap_year)

# Getting a string representation of a month's calendar
month_calendar = calendar.month(2023, 6)
print("June 2023 calendar:")
print(month_calendar)

# Printing a calendar for the year
calendar.prcal(2023)

# Printing a calendar for a specific month
calendar.prmonth(2023, 6)

# Setting the first day of the week (0 for Monday, 6 for Sunday)
calendar.setfirstweekday(calendar.SUNDAY)
print("First day of the week set to Sunday")

# Getting the Unix timestamp for a specific date and time
timestamp = calendar.timegm((2023, 6, 15, 0, 0, 0))
print("Unix timestamp for June 15, 2023:", timestamp)

# Getting the weekday (0 for Monday, 6 for Sunday) for a specific date
weekday = calendar.weekday(2023, 6, 15)
print("Weekday for June 15, 2023:", weekday)
