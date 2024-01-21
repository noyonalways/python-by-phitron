# Day - 06: Simple problem solving

| Problem Solving                                                                      |
| ------------------------------------------------------------------------------------ |
| 6.1 [Python program to print a multiplication table of a given number](#problem---1) |
| 6.2 [Python program to find the factorial of a given number](#problem---2)           |
| 6.3 [Fibonacci series](#problem---3)                                                 |
| 6.4 [Count the number of digit count in a number](#problem---4)                      |
| 6.5 [Python Program to check Armstrong Number](#problem---5)                         |
| 6.6 [Integer number reverse](#problem-6)                                             |

## Problem - 1

```python
# Python program to print a multiplication table of a given number
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(number, " X ", i, " = ", number * i)
```

## Problem - 2

```python
# Python program to find the factorial of a given number
number = int(input("Enter a number: "))
factorial = 1
for i in range(1, number + 1):
    factorial = factorial * i
print(factorial)
```

## Problem - 3

```python
# Fibonacci series
a = 0
b = 1
# a, b = 0, 1 --> for shorcut

for i in range(10):
    print(a, end= " ")
result = a + b
a = b
b = result
```

## Problem - 4

```python
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
```

## Problem - 5

```python
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
```

```python
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
```

## Problem 6

```python
# Integer number reverse
a = int(input())
revers = 0
while a > 0:
    last_digit = a % 10
    revers = revers * 10 + last_digit
    # a = a // 10
    a //= 10
print(revers)
```
