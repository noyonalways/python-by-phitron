# String indexing and immputability in Python

message = "Hello World"
         #012345678910 => index
         # -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

print(message[10]) # d
print(message[-1]) # d

message[-1] = "D" #' str' object does not support item assignment


for i in message:
   print(i)

for i in range(len(message)):
   print(message[i], end= " ")

# slicing
print(message[1:10:3])