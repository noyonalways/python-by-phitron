# Problem - 3
# Fibonacci series

a = 0
b = 1
# a, b = 0, 1 --> for shorcut 

for i in range(10):
    print(a, end= " ")
    result = a + b
    a = b
    b = result