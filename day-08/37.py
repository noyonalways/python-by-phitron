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