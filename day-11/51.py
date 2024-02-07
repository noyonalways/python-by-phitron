# Lecture 4: Palindrome string checking
# Example: Madam
# input: "Madam"
# output: "Yes"

user_input = input("Enter input: ")
if user_input == user_input[::-1]:
  print("Yes")
else:
  print("No")