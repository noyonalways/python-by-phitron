# break keyword

for i in range(10):
    print(i) # --> 1, 2, 3, 4, 5
    if i == 5:
        break
    print(i) # --> 1, 2, 3, 4,



a = 0
while a <= 10:
    a = a + 1
    print(a) # --> 1, 2, 3, 4, 5
    if a == 5:
        break
    print(a) # --> 1, 2, 2, 4
