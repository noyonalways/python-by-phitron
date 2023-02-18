# Problem 5: Write a Program to check whether a year is leap year or not. Take input from User.
# example: if year = 1996, it is a leap year
# Conditions for leap year:
# - 1. If a year is divisible by both 400 and 100 it is a leap year.
# - 2. If a year is divisible by 4 and not divisible by 100 it is a leap year.

year = int(input("Enter a year: "))



# Method 1:

if year % 400 == 0:
    print(year, "is a Leap year.")
elif year % 100 == 0:
    print(year, "is not a Leap year.")
elif year % 4 == 0:
    print(year, "is a Leap year.")
else:
    print(year, "is not a Leap year.")


# Method 2:

if year % 400 == 0 and year % 100 == 0:
    print(year, "is a Leap year.")
elif year % 4 == 0 and year % 100 != 0:
    print(year, "is a Leap year.")
else:
    print(year, "is not a Leap year.")


# Method 3:

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap year.")
else:
    print(year, "is not a Leap year.")