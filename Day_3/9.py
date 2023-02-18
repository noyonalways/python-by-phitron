# Problem 2: Take three integer input from user and find the largest number between using if-elif-else statement

number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
number_3 = int(input("Enter the third number: "))

# Method 1: --> Using Nested if-else

if number_1 > number_2:
    if number_1 >= number_3:
        print(number_1, 'is the Largest number.')
    else:
        print(number_3, 'is the Largest number.')
else:
    if number_2 >= number_3:
        print(number_2, 'is the Largest number.')
    else:
        print(number_3, 'is the Largest number.')




# Method 2: --> Using Logical Operator

if number_1 >= number_2 and number_1 >= number_3:
    print(number_1, "is the Largest number.")
elif number_2 >= number_1 and number_2 >= number_3:
    print(number_2, "is the Largest number.")
else:
    print(number_3, "is the Largest number.")
