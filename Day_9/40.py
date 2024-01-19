# Problem 1: Swaping to list elements
num_list = [17, 11, 12, 13, 14, 15, 16, 10]
temp = num_list[0]
num_list[0] = num_list[-1] # a[len(num_list) - 1]
num_list[-1] = temp
print(num_list)