# Day - 10

<img width="100%" style="border-radius: 5px; background: #fff" src="https://i1.faceprep.in/feed/images/strings-in-python-poster.webp" alt="illustration-image" />

| Introduction to String in Python                                                                     |
| ---------------------------------------------------------------------------------------------------- |
| 10.1 [Introduction to sting in Python](#introduction-to-string-in-python)                            |
| 10.2 [Indexing and immutability of string in Python](#indexing-and-immutability-of-string-in-python) |
| 10.3 [String methods part 1](#string-methods-part-1)                                                 |
| 10.4 [String methods part 2](#string-methods-part-2)                                                 |

## Introduction to string in Python

```python
# Welcome to day 11
# Introduction to string in Python

'''
- string is imutable
- ordered data type
- indexing same as list

'''

# 3 types of strings declaration
a = 'Hello World'
b = "Hello World"
c = """This is a
multipe line string
"""
```

## Indexing and immutability of string in Python

```python
# String indexing and immputability in Python

message = "Hello World"
         #012345678910 => index
         # -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

print(message[10]) # d
print(message[-1]) # d

message[-1] = "D" #' str' object does not support item assignment


for i in message:
   print(i)

for i in range(len(message)):
   print(message[i], end= " ")

# slicing
print(message[1:10:3])
```

## String methods part 1

```python
# String methods part 1
message = "Hello World Python"

# lower(): converts characters into lowercase
lowercase_message = message.lower() # returns new string
print(lowercase_message)

# upper(): coverts characters into uppercase
uppercase_message = message.upper() # returns new string
print(uppercase_message)

# title(): converts string to title case or capitalize
titlecase_message = message.title() # returns new string
print(titlecase_message)

# islower() returns boolean {True or False}
text_1 = "hello"
print(text_1.islower()) # returns True

# isupper() returns boolean {True or False}
text_2 = "HELLO"
print(text_2.isupper()) # returns True

# istitle() returns boolean {True or False}
text_3 = "Hello"
print(text_3.istitle()) # returns True

# isalpha() returns boolean {True or False}
new_text = "hello123"
print(new_text.isalpha()) # returns False
```

## String methods part 2

```python
# String methods part 2
message = "Hello World Python"

# capitalize()
print(message.capitalize())

# title()
print(message.title())

# swapcase()
text_message = "hELLO WORLD"
print(text_message.swapcase())

# casefold() text = "groß"
text = "groß"
print(text.lower()) # can't convert groß
print(text.casefold()) # converts gross

# replace()
# replace("what", "new", "count")
text_1 = "HEllo"
text_2 = text_1.replace(text_1[1], "e", 1)
print(text_1) # don't change the original string
print(text_2) # returns a new string

# count()
name = "noyon"
print(name.count('n'))

# isdigit()
user_input = 'H19'
print(user_input.isdigit())

# join() it only works on string
char_list = ["h", "e", "l", "l", "o"]
print("".join(char_list)) # returns hello
num_list = ["1", "2", "3"]
print("".join(num_list))

# list()
new_text = 'hello'
print(list(new_text)) # ['h', 'e', 'l', 'l', 'o']

# split()
print(new_text.split()) # ['hello']
```
