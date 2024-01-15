# List slicing
custom_list = [1, 2, 3, 4, 5]
reverse_list = custom_list[::-1] # create new reverse list with different referance
another_reverse_list = custom_list[-1::-1] # create new reverse list with different referance
empty_list = custom_list[-1:-1:-1] # return empty list
new_slice = custom_list[::2]
print(empty_list)

# slice tecnique works: [start:end:step]