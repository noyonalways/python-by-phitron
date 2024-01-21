# Problem 3: Given a list, extract all elements whose frequency is greter than K. 
#num_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8] K = 3

num_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
K = 3
result_list = []

for i in num_list:
   freq = num_list.count(i)
   if freq > K and i not in result_list:
      result_list.append(i)

print(result_list)