# Problem 3: Write a program using conditional Statement whether a number is even or odd. (even means divisible by 2 and odd mean not divisible by 2)
# Suppose user provide input as 15 then it will print "15 is an odd number"


user_number = int(input("Enter a number: "))
if user_number % 2 == 0:
    print(user_number, 'is a even number.') 
else:
    print(user_number, 'is a odd number.')
