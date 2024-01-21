# String methods part 2
message = "Hello World Python"

# capitalize()
print(message.capitalize())

# title()
print(message.title())

# swapcase()
text_message = "hELLO WORLD"
print(text_message.swapcase())

# casefold() text = "groß"
text = "groß"
print(text.lower()) # can't convert groß
print(text.casefold()) # converts gross

# replace()
# replace("what", "new", "count")
text_1 = "HEllo"
text_2 = text_1.replace(text_1[1], "e", 1)
print(text_1) # don't change the original string
print(text_2) # returns a new string

# count()
name = "noyon"
print(name.count('n'))

# isdigit()
user_input = 'H19'
print(user_input.isdigit())

# join() it only works on string
char_list = ["h", "e", "l", "l", "o"]
print("".join(char_list)) # returns hello
num_list = ["1", "2", "3"]
print("".join(num_list))

# list()
new_text = 'hello'
print(list(new_text)) # ['h', 'e', 'l', 'l', 'o']

# split()
print(new_text.split()) # ['hello']