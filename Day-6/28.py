# Problem - 4
# Count the number of digit count in a number


# Method 1: longcut

number = int(input())

count = 0
while number > 0:
    count = count + 1
    number = number // 10
print(count)


# Method 2: shorcut

a = input()
print(len(a))
