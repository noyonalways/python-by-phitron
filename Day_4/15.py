for i in range(10):
    print(i)

b = list(range(10))        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
c = list(range(2, 10))     # [2, 3, 4, 5, 6, 7, 8, 9]
d = list(range(3, 10))     # [3, 4, 5, 6, 7, 8, 9]
e = list(range(0, 10, 2))  # [0, 2, 4, 6, 8]
f = list(range(0, 10, 3))  # [0, 3, 6, 9]
print(b) 
print(c)
print(d)
print(e)
print(f)

y = list(range(10, 0, -2)) # [10, 8, 6, 4, 2]
print(y)