# List built in methods
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b; # it will combined a and b list item into one list
# print(c) 

# list() convert list to string
message = 'Hello World!'
text_to_list = list(message)
# print(text_to_list)


# append() adds an element at the ene of a list
num_list = [10, 11, 12, 13, 14, 15]
new_num_list = num_list.append(16) # The append() method returns nothing!
# print(num_list)

# insert() adds an element at the specified position
num_list.insert(len(num_list), 17)
# print(num_list)


# copy() returns copy of the list
copy_list = num_list.copy()
# print(copy_list)


# count() returns the number of element with the specified value
duplicate_num_list = [1, 2, 3, 4, 4, 4, 4, 4, 5, 4]
count_dupicates = duplicate_num_list.count(4)
# print(count_dupicates)
# print(duplicate_num_list.count('a')) # it will return 0 because there is no 'a' in this list


# extend() add the elements of a list to the end of the current list
random_num = [1, 3, 2]
random_num2 = [4, 7, 9]
final_list = random_num.extend(random_num2) # extend() retuns nothing!
print(random_num)
