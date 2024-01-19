# Problem 2: Count unique elements in a list
number_list = [1, 2, 2, 3, 3, 3, 4, 5, 6]
unique_number_list = []
unique_number_count = 0

for i in number_list:
   if i not in unique_number_list:
      unique_number_count = unique_number_count + 1
      unique_number_list.append(i)

print(unique_number_count)
print(unique_number_list)