# Day - 07


| List in Python                                              |
| ----------------------------------------------------------- |
| 7.1 [Introduction to list in Python](#introduction-to-list) |
| 7.2 [More about list indexing](#more-about-list-indexing)   |
| 7.3 [List slicing like slicing a cake]()                    |
| 7.4 [List methods Part -1]()                                |
| 7.5 [List methods Part -2]()                                |



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