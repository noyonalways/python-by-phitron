# Problem 1: Take values of length and breadth of a rectangle from user and check if it is square or not.

lenght = int(input("Enter the lenght of the rectangle: "))
breadth = int(input("Enter the breadth of the rectangle: "))

if lenght == breadth:
    print("This is a Square.")
else:
    print("This is a Rectangular.")