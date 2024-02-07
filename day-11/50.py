# Lecture 3: Simple Problem solving string sorting
# Input : x3b4U5i2
# Output : bbbbiiUUUUUxxx
user_input = input("Enter input: ")
res = ""
for i in range(0, len(user_input), 2):
  print(f"{user_input[i]} {user_input[i+1]}")
  res = res + user_input[i]*int(user_input[i+1])
result = sorted(res, key=str.casefold)
result_string = "".join(result)
print(result_string)