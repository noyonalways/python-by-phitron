# Problem 4: Write a Program to take integer input from user and display the grade according to the following criteria.
# > 90 - 100      --> A
# > 80 and <= 90   --> B
# >= 60 and <= 80   --> C
# below 60         --> D

marks = int(input("Enter your marks: "))

if marks > 90:
    print("Your Grade is A")
elif marks > 80 and marks <= 90:
    print("Your Grade is B")
elif marks >= 60 and marks <= 80:
    print("Your Grade is C")
else:
    print("Your Grade is D")