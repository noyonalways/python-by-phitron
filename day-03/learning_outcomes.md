# Day - 03: Solve the problems from day-1 and day-2

## Slove the problems from Day-1 and Day-2

| Solutions                                     |
| --------------------------------------------- |
| 3.1 [Solution to Practice Problem 1](./8.py)  |
| 3.2 [Solution to Practice Problem 2](./9.py)  |
| 3.3 [Solution to Practice Problem 3](./10.py) |
| 3.4 [Solution to Practice Problem 4](./11.py) |
| 3.5 [Solution to Practice Problem 5](./12.py) |

### Problem 1 Square check:

```python
length = int(input('input length: '))
breadth = int(input('input breadth: '))
if length == breadth:
    print('it is square')
else:
    print('it is not square')
```

### Problem 2: Find larg number:

```python
a = int(input('input a : '))
b = int(input('input b : '))
c = int(input('input c : '))
if a >= b and a >= c:
    print(a, 'a is larg number rather than others')
elif b >= a and b >= c:
    print(b, 'b is a large number rather than others')
elif c >= a and c >= b:
    print(c, 'c is a large number rather than others')
```

### Problem 3: Check even or odd number:

```python
number = int (input('input number for check even or odd: '))
if number % 2 == 0:
    print(number, ': it is even number')
else:
    print(number, ': it is odd number')
```

### Problem 4: Write a Program to take integer input from user and display the grade according to the following criteria:

```python
studentMarks = int(input())
if studentMarks > 90:
    print(studentMarks, ": Grade A")
elif studentMarks > 80 and studentMarks <= 90:
    print(studentMarks, ": Grade b")
elif studentMarks >= 60 and studentMarks <= 80:
    print(studentMarks, ": Grade c")
elif studentMarks < 60 :
    print(studentMarks, ": Grade d")
```

### Problem 5: Check leap year:

```python
inputYear = int(input('input year: '))
if inputYear % 100 == 0 and inputYear % 400 == 0:
    print(inputYear, ': it is leap year')
elif inputYear % 4 == 0 and inputYear % 100 != 0:
    print(inputYear, ': it is leap year')
else:
    print(inputYear, 'it is not leap year')
```
