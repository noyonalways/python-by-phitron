# Day - 07

| List in Python                                              |
| ----------------------------------------------------------- |
| 7.1 [Introduction to list in Python](#introduction-to-list) |
| 7.2 [More about list indexing](#more-about-list-indexing)   |
| 7.3 [List slicing like slicing a cake](#list-slicing)       |
| 7.4 [List methods Part-1](#list-methods-part-1)             |
| 7.5 [List methods Part-2](#list-methods-part-2)             |

## Introduction to List

Example of List:

    a =  ["Mango", "Banana", "Apple"] --> 1D List
    b =  [[11, 12], ["Cake"], [-22]] --> 2D list / Nested list

#### About list:

1. List is a Data structure
2. It can contains Different type data
3. It's an Ordered Data structure
4. It is a Mutable Data structure

---

## More about list indexing

Indexing is two types:

1. Positive indexing -> [0, 1, 2, 3, 4]
2. Negetive indexing <- [-4, -3, -2, -1]

### Examples:

    a = [12, 20, 34, "Phitron"]
    print([0])
    print(a[-3])

    print(a[-20]) # Height index - 4 is possible

    print(len(a))

    a[-3] = 500 # Changed in Memory
    print(a)

    if 500 in a:
        print("Found")
    else:
        print("Not found")

### Traversing:

    a = [12, 20, 34, "Phitron"]

    for i in a:
        print(i)

    Positive indexing
    for i in range(len(a)):
        print(i, a[i])


    Negetive indexing --> Reviersing
    for i in range(-1, -len(a)-1, -1):
        print(i, a[i])

    Positive indexing --> Reversing
    for i in range(len(a)-1, -1, -1):
        print(i, a[i])

### List slicing

    custom_list = [1, 2, 3, 4, 5]
    reverse_list = custom_list[::-1] # create new reverse list with different referance
    another_reverse_list = custom_list[-1::-1] # create new reverse list with different referance
    empty_list = custom_list[-1:-1:-1] # return empty list
    new_slice = custom_list[::2]
    print(empty_list)

    # slice tecnique works: [start:end:step]

### List methods part-1

- list() convert list to string

```
message = 'Hello World!'
text_to_list = list(message)
print(text_to_list)
```

- append() adds an element at the ene of a list

```
num_list = [10, 11, 12, 13, 14, 15]
new_num_list = num_list.append(16) -> The append() method returns nothing!
print(num_list)
```

- insert() adds an element at the specified position

```
num_list.insert(len(num_list), 17)
print(num_list)
```

- copy() returns copy of the list

```
copy_list = num_list.copy()
#print(copy_list)
```

- count() returns the number of element with the specified value

```
duplicate_num_list = [1, 2, 3, 4, 4, 4, 4, 4, 5, 4]
count_dupicates = duplicate_num_list.count(4)
print(count_dupicates)
print(duplicate_num_list.count('a')) -> it will return 0 because there is no 'a' in this list
```

- extend() add the elements of a list to the end of the current list

```
random_num = [1, 3, 2]
random_num2 = [4, 7, 9]
final_list = random_num.extend(random_num2) -> extend() retuns nothing!
print(random_num)
```

### List methods part-2

- pop() the pop method removes the element at the specified positon and returns removed value

```
numbers = [1, 2, 3, 4, 5]
updated_list = numbers.pop() -> returns removed value as it was 5
print(updated_list)
```

- remove() the remove method removes the first occurrence of the element with the specified value

```
num_list = [1, 2, 3, 4, 5]
removed_list = num_list.remove(5) -> it returns nothing!
print(removed_list)
```

- clear() the clear method removes all the elements from a list

```
cleard_list = num_list.clear() -> it returns nothing!
print(num_list)
```

- reverse() the reverse() method reverses the sorting order of the elements

```
new_list = [10, 11, 12, 13, 14, 15]
reversed_list = new_list.reverse() -> it returns nothing!
print(new_list)
```

- sort() sort a list in ascending and descending ordered

```
random_numbers = [1, 3, 4, 5 , -2, -1, 0]
ascending_ordered= random_numbers.sort() -> it returns nothing!
descending_ordered= random_numbers.sort(reverse=True) -> it returns nothing!
print(random_numbers)
```

- max() function returns the item with the highest value, or the item with the highest value in an iterable. If the values are strings, an alphabetically comparison is done

```
all_numbers = [1, 2, 3, 4, 45, 60, 99]
max_value = max(all_numbers) -> returns the max value
print(max_value)
min_value = min(all_numbers) -> returns the min value
print(min_value)
```
