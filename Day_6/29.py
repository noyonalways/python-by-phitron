# Problem - 5
# Python Program to check Armstrong Number


# Method 1
a = int(input())
num_len = len(str(a))
temp = a
sum = 0
while temp > 0:
    lst_digit = temp % 10
    sum = sum + lst_digit ** num_len
    temp = temp // 10
    # temp //= 10
if sum == a:
    print(a, "is a Armstrong Number")
else:
    print(a, "is a Not Armstrong Number!")



# Method 2
a = input()
num_len = len(a)
sum = 0
for i in a:
    sum = sum + int(i) ** num_len
    # sum += int(i) ** num_len

if int(a) == sum:
    print(a, "is a Armstrong Number")
else:
    print(a, "is a Not Armstrong Numbe!")