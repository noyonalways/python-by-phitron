# Welcome to Day - 8

<img style="border-radius: 5px" src="https://training-blog-uploads.internshala.com/blog/wp-content/uploads/2023/06/python-list-comprehension-2048x854.jpg.webp" alt="illustration-image" />

| List comprehension in Python                                                                      |
| ------------------------------------------------------------------------------------------------- |
| 8.1 [Introduction to list comprehension in Python](#introduction-to-list-comprehension-in-python) |
| 8.2 [List Comprehension: part - 1](#list-comprehension-part---1)                                  |
| 8.3 [List comprehension: part - 2](#list-comprehension-part---2)                                  |

## Introduction to list comprehension in Python

_Taking mutiple inputs from user and store it in a list_

```python
# problem 1: taking multiple string input
user_input = input().split()
print(user_input)

# problem 2: taking multiple int input
int_number_input = list(map(int, input("Enter int numbers: ").split()))
print(int_number_input)

# problem 3: takinmg multiple float input
float_number_input = list(map(float, input("Enter float nubers: ").split()))
print(float_number_input)
```

## List Comprehension: part - 1

```python
# List comprehension: part - 1
# [expresssion for item in list]
# Code less do more!

# Example 1: Iteration with list comprehension
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_2 = [i+5 for i in list_1]
print(list_2)

# Example 2: Iterating through a string using list comprehension
text = "Hello World"
string_list = [i for i in text]
text_list = list(text) # shortcut
print(string_list)

# Example 3: Using range() funciton in list comprehension
odd_num_list = [i for i in range(1, 20, 2)]
even_num_list = [i for i in range(2, 21, 2)]
num_list = list(range(2, 21, 2)) # shortcut
print(odd_num_list)
print(even_num_list)
```

## List comprehension: part - 2

```python
# List comprehension: part - 2
# [expression(element) for element in list if condition]

# Example 4: Using if with list comprehension
numbers_1 = []
for i in range(1, 20):
   if i % 3 == 0:
      numbers_1.append(i)
print(numbers_1)
num_list_1 = [i for i in range(1, 20) if i % 3 == 0] # shortcut way
print(num_list_1)

# Example 5: Nested if with list comprehension
numbers_2 = []
for i in range(1, 20):
   if i % 3 == 0:
      numbers_2.append(i)
   if i % 5 == 0:
      numbers_2.append(i)
print(numbers_2)
num_list_2 = [i for i in range(1, 20) if i % 3 == 0 or i % 5 == 0] # shortcut way
print(num_list_2)

# Example 6: if...else wiht list comprehension
# [if else for i in list]
empty_list = []
for i in range(21):
   if i % 2 == 0:
      empty_list.append(f"{i}=even")
   else:
      empty_list.append(f"{i}=odd")
print(empty_list)
empty_list_2 = [f"{i}=even" if i % 2 == 0 else f"{i}=odd" for i in range(21)] # shortcut way
print(empty_list_2)
```
