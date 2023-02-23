# Problem 6
# Integer number reverse

a = int(input())
revers = 0
while a > 0:
    last_digit = a % 10
    revers = revers * 10 + last_digit
    # a = a // 10
    a //= 10
print(revers)