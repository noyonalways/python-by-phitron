# More about foor loop
words = "Hello World"
for latter in words:
    print(latter)


# print item
bag = ["Alu", "Piyaj", "Morich", 30, 25, 11, 0, 5, 3]
for item in bag:
    print(item)



# 3 and 5 dhara divisible number ber korar jonno
for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        print(i) # [0, 15, 30, 45, 60, 75, 90]


# Sum calculate
sum = 0
for i in range(1, 11):
    sum = sum + i

print("1 to 10 total is:", sum) # [55]