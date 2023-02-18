# Python Logical operators
# and, or, not

'''
print(10 - 4 == 6 and 10 - 5 == 15) # return Flase
print(10 - 4 == 6 and 10 -5 == 5) # return True
print(10 - 4 == 6 or 10 - 5 == 15) # return True
print(10 - 4 == 6 or 10 - 5 == 5) # return True
print(not(10 - 4) == 6) # return False 
'''

marks = 79

if marks >= 90 and marks <= 100:
    print("Tumi 2 Ta candy box paba.")
elif marks >= 80 and marks <= 89:
    print("Tumi 1 ta candy box paba.")
else:
    print("Tumi kisoi paba na!")