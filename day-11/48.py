# Day 11 
# Lecture 1: More about string in Python
# Todays topic: String formatting

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