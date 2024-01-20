# String methods part 1
message = "Hello World Python"

# lower(): converts characters into lowercase
lowercase_message = message.lower() # returns new string
print(lowercase_message)

# upper(): coverts characters into uppercase
uppercase_message = message.upper() # returns new string
print(uppercase_message)

# title(): converts string to title case or capitalize
titlecase_message = message.title() # returns new string
print(titlecase_message)

# islower() returns boolean {True or False}
text_1 = "hello"
print(text_1.islower()) # returns True

# isupper() returns boolean {True or False}
text_2 = "HELLO"
print(text_2.isupper()) # returns True

# istitle() returns boolean {True or False}
text_3 = "Hello"
print(text_3.istitle()) # returns True

# isalpha() returns boolean {True or False}
new_text = "hello123"
print(new_text.isalpha()) # returns False