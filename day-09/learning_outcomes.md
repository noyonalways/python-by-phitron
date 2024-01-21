# Day - 9: Swap, Count unique elements, extract elements, crete nested list using list comprehesion

<img width="100%" style="border-radius: 5px" src="https://community-cdn-digitalocean-com.global.ssl.fastly.net/RoGkayKbiUPPDfVJa56gTwmy" alt="illustration-image" />

| List comprehension in Python                                                          |
| ------------------------------------------------------------------------------------- |
| 9.1 [Swap two list elements in a list](#problem-1-swaping-to-list-elements)           |
| 9.2 [Count unique elements in an list](#problem-2-count-unique-elements-in-a-list)    |
| 9.3 [Extract elements from a list](#problem-3-extract-elements-from-a-list)           |
| 9.4 [Create a list using list comprehension](#create-a-list-using-list-comprehension) |

## Problem 1: Swaping to list elements

```python
# Problem 1: Swaping to list elements
num_list = [17, 11, 12, 13, 14, 15, 16, 10]
temp = num_list[0]
num_list[0] = num_list[-1] # a[len(num_list) - 1]
num_list[-1] = temp
print(num_list)
```

## Problem 2: Count unique elements in a list

```python
# Problem 2: Count unique elements in an list
number_list = [1, 2, 2, 3, 3, 3, 4, 5, 6]
unique_number_list = []
unique_number_count = 0

for i in number_list:
   if i not in unique_number_list:
      unique_number_count = unique_number_count + 1
      unique_number_list.append(i)

print(unique_number_count)
print(unique_number_list)
```

## Problem 3: Extract elements from a list

```python
# Problem 3: Given a list, extract all elements whose frequency is greter than K.
# num_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8] K = 3

num_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
K = 3
result_list = []

for i in num_list:
   freq = num_list.count(i)
   if freq > K and i not in result_list:
      result_list.append(i)

print(result_list)
```

## Create a list using list comprehension

```python
# Problem 4: create the following list using list comprehension
# [[1, 2, 3, 4], [0, 2, 3, 4], [0, 1, 3, 4], [0, 1, 2, 4], [0, 1, 2, 3]]

num_list = [[j for j in range(5) if i !=j] for i in range(5)]
print(num_list)
```
