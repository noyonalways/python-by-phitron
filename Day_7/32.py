# More about indexing

'''
Indexing is two types:
    1. Positive indexing -> [0, 1, 2, 3, 4]
    2. Negetive indexing <- [-4, -3, -2, -1]
'''

a = [12, 20, 34, "Phitron"]
# print([0])
# print(a[-3])
# # print(a[-20]) --> Height - 4 is possible
# print(len(a))

# a[-3] = 500 # Changed in Memory that meanes mutable
# print(a)

# if 500 in a:
#     print("Found")
# else:
#     print("Not found")


# Traversing

for i in a:
    print(i)


# Positive indexing
for i in range(len(a)):
    print(i, a[i])


# Negetive indexing --> Reviersing
for i in range(-1, -len(a)-1, -1):
    print(i, a[i])

# Positive indexing --> Reversing
for i in range(len(a)-1, -1, -1):
    print(i, a[i])

b = [[12, 13], [18, 23, "Phitron"], [-1, 19]]
b[0][1] = 200
# b[0][2] = 300 # list assignment index out of range
print(b[0][1])
