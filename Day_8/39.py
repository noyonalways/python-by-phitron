# 2D List comprehension
matrix = [
   [1, 2], 
   [3, 4], 
   [5, 6], 
   [7, 8]
]

# transpose matrix e conversion
empty_list = [] 
for row in range(2): # outer loop
   b = []
   for col in matrix: # inner loop
      b.append(col[row])
   empty_list.append(b)
print(empty_list)

# shortcut way by comprehension
result = [[col[row] for col in matrix] for row in range(2)]
print(result)