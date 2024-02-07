# Lecture 5: Reversing
# input: "I love coding using Python"
# output: "I evol gnidoc gnisu nohtyP"

user_input = input("Enter input: ")
user_input = user_input.split(" ")
print(user_input)
result = ""
for i in user_input:
  result += i[::-1] + " "

print(result)