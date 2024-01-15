# More list methods - part: 2

# pop() the pop method removes the element at the specified positon and returns removed value
numbers = [1, 2, 3, 4, 5]
updated_list = numbers.pop() # returns removed value as it was 5
# print(updated_list)


# remove() the remove method removes the first occurrence of the element with the specified value
num_list = [1, 2, 3, 4, 5]
removed_list = num_list.remove(5) # it returns nothing!
# print(removed_list)


# clear() the clear method removes all the elements from a list
cleard_list = num_list.clear() # it returns nothing!
# print(num_list)


# reverse() the reverse() method reverses the sorting order of the elements
new_list = [10, 11, 12, 13, 14, 15]
reversed_list = new_list.reverse() # it returns nothing!
# print(new_list)


# sort() sort a list in ascending and descending ordered
random_numbers = [1, 3, 4, 5 , -2, -1, 0]
ascending_ordered= random_numbers.sort() # it returns nothing!
descending_ordered= random_numbers.sort(reverse=True) # it returns nothing!
# print(random_numbers)


# max() function returns the item with the highest value, or the item with the highest value in an iterable. If the values are strings, an alphabetically comparison is done.
all_numbers = [1, 2, 3, 4, 45, 60, 99]
max_value = max(all_numbers) # returns the max value
# print(max_value)
min_value = min(all_numbers) # returns the min value
# print(min_value)