# Day - 11: String Formatting, concatenation, and simple problem solving

<img width="100%" style="border-radius: 5px; background: #fff" src="https://i1.faceprep.in/feed/images/strings-in-python-poster.webp" alt="illustration-image" />

## Lecture 1: String formatting

```py
# Method 1:
name = "Rahim"
age = 20
template_string1 = "I am {}. I am {} years old".format(name, age) # 1
print(template_string1)
template_string2 = "I am {1}. I am {0} years old".format(age, name) # 2
print(template_string2)
template_string3 = "I am {first_name}. I am {user_age} years old".format(user_age=25, first_name="Karim") # 3
print(template_string3)

# Method 2:
text_string = f"I am {name}. I am {age + 2} years old"
print(text_string)
```

## Lecture 2: String Concatenation

```py
string_1 = "Hello"
string_2 = "xyz"
new_string_1 = string_1+string_2
new_string_2 = string_1+", " +string_2
print(new_string_1)
print(new_string_2)

# 2^3 = 2*2*2
print("Hello world, "*3)
```

### Lecture 3: Simple Problem solving string sorting

```py
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
```

## Lecture 4: Palindrome string checking

```py
# Example: Madam
# input: "Madam"
# output: "Yes"

user_input = input("Enter input: ")
if user_input == user_input[::-1]:
  print("Yes")
else:
  print("No")
```

## Lecture 5: Reversing

```py
# input: "I love coding using Python"
# output: "I evol gnidoc gnisu nohtyP"

user_input = input("Enter input: ")
user_input = user_input.split(" ")
print(user_input)
result = ""
for i in user_input:
  result += i[::-1] + " "

print(result)
```
