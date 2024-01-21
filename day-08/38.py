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