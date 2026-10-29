# Data Structures & Algorithms — Mid-Sem Exam Notes

## Instructions / Exam Style

- Language: **Python 3**
- Every input is taken from the **user**.
- Do **not** use built-in sorting/searching functions such as `sort()`, `sorted()`, `index()`, etc.
- For each experiment:
  1. Algorithm / Pseudocode
  2. Python 3 Program
  3. Sample Output
  4. Time Complexity
  5. Space Complexity
- Answers are kept short and easy to reproduce in an exam.

---

# 1. Binary Search

### Algorithm

```text
BinarySearch(A, key)
1. Set low = 0, high = n - 1
2. Repeat while low <= high:
   a. mid = (low + high) // 2
   b. If A[mid] == key, return mid
   c. If key < A[mid], high = mid - 1
   d. Else low = mid + 1
3. Return -1 if key is not found
```

### Python Program

```python
n = int(input("Enter number of elements: "))
a = []

print("Enter sorted elements:")
for i in range(n):
    a.append(int(input()))

key = int(input("Enter key to search: "))

low = 0
high = n - 1
found = -1

while low <= high:
    mid = (low + high) // 2

    if a[mid] == key:
        found = mid
        break
    elif key < a[mid]:
        high = mid - 1
    else:
        low = mid + 1

if found != -1:
    print("Key found at index:", found)
else:
    print("Key not found")
```

### Sample Output

```text
Enter number of elements: 5
Enter sorted elements:
10
20
30
40
50
Enter key to search: 30
Key found at index: 2
```

### Complexity

- **Time:** O(log n)
- **Space:** O(1)

---

# 2. Find Bitonic Point

A bitonic sequence first increases and then decreases. The bitonic point is the maximum element.

### Algorithm

```text
FindBitonic(A)
1. Set low = 0, high = n - 1
2. While low <= high:
   a. mid = (low + high) // 2
   b. If A[mid] > A[mid-1] and A[mid] > A[mid+1],
      return mid
   c. If A[mid] < A[mid+1], search right half
   d. Else search left half
3. Return the found index
```

### Python Program

```python
n = int(input("Enter number of elements: "))
a = []

print("Enter bitonic sequence:")
for i in range(n):
    a.append(int(input()))

low = 0
high = n - 1

while low <= high:
    mid = (low + high) // 2

    if mid == 0:
        if a[0] > a[1]:
            print("Bitonic point:", a[0])
            print("Index:", 0)
            break
        else:
            low = mid + 1

    elif mid == n - 1:
        if a[n - 1] > a[n - 2]:
            print("Bitonic point:", a[n - 1])
            print("Index:", n - 1)
            break
        else:
            high = mid - 1

    elif a[mid] > a[mid - 1] and a[mid] > a[mid + 1]:
        print("Bitonic point:", a[mid])
        print("Index:", mid)
        break

    elif a[mid] < a[mid + 1]:
        low = mid + 1

    else:
        high = mid - 1
```

### Sample Output

```text
Enter number of elements: 7
Enter bitonic sequence:
2
5
8
12
10
7
3
Bitonic point: 12
Index: 3
```

### Complexity

- **Time:** O(log n)
- **Space:** O(1)

---

# 3. Selection Sort

### Algorithm

```text
SelectionSort(A)
1. For i = 0 to n-2:
2.    Set min = i
3.    For j = i+1 to n-1:
4.       If A[j] < A[min], set min = j
5.    Swap A[i] and A[min]
6. Display sorted array
```

### Python Program

```python
n = int(input("Enter number of elements: "))
a = []

for i in range(n):
    a.append(int(input("Enter element: ")))

for i in range(n - 1):
    min_pos = i

    for j in range(i + 1, n):
        if a[j] < a[min_pos]:
            min_pos = j

    temp = a[i]
    a[i] = a[min_pos]
    a[min_pos] = temp

print("Sorted array:", end=" ")
for i in range(n):
    print(a[i], end=" ")
```

### Sample Output

```text
Enter number of elements: 5
Enter element: 64
Enter element: 25
Enter element: 12
Enter element: 22
Enter element: 11
Sorted array: 11 12 22 25 64
```

### Complexity

- **Time:** O(n²)
- **Space:** O(1)

---

# 4. Optimized Bubble Sort

Optimization: If no swapping occurs during a pass, the array is already sorted.

### Algorithm

```text
BubbleSort(A)
1. For i = 0 to n-2:
2.    Set swapped = False
3.    For j = 0 to n-i-2:
4.       If A[j] > A[j+1]:
5.          Swap them
6.          Set swapped = True
7.    If swapped is False, stop
```

### Python Program

```python
n = int(input("Enter number of elements: "))
a = []

for i in range(n):
    a.append(int(input("Enter element: ")))

for i in range(n - 1):
    swapped = False

    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp
            swapped = True

    if swapped == False:
        break

print("Sorted array:", end=" ")
for i in range(n):
    print(a[i], end=" ")
```

### Sample Output

```text
Enter number of elements: 5
Enter element: 5
Enter element: 1
Enter element: 4
Enter element: 2
Enter element: 8
Sorted array: 1 2 4 5 8
```

### Complexity

- **Best Time:** O(n)
- **Average/Worst Time:** O(n²)
- **Space:** O(1)

---

# 5. Stack — Push, Pop and Peek

### Algorithm

```text
PUSH(x)
1. If stack is full, display Overflow
2. Else increment top and insert x

POP()
1. If stack is empty, display Underflow
2. Else display and remove top element

PEEK()
1. If stack is empty, display Empty
2. Else display top element
```

### Python Program

```python
stack = []
top = -1
size = int(input("Enter stack size: "))

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        if top == size - 1:
            print("Stack Overflow")
        else:
            x = int(input("Enter element: "))
            stack.append(x)
            top += 1

    elif choice == 2:
        if top == -1:
            print("Stack Underflow")
        else:
            print("Popped:", stack[top])
            stack.pop()
            top -= 1

    elif choice == 3:
        if top == -1:
            print("Stack is empty")
        else:
            print("Top element:", stack[top])

    elif choice == 4:
        if top == -1:
            print("Stack is empty")
        else:
            print("Stack:", stack)

    elif choice == 5:
        break

    else:
        print("Invalid choice")
```

### Sample Output

```text
Enter stack size: 3

1. Push
2. Pop
3. Peek
4. Display
5. Exit
Enter choice: 1
Enter element: 10

Enter choice: 1
Enter element: 20

Enter choice: 3
Top element: 20

Enter choice: 2
Popped: 20
```

### Complexity

- **Push:** O(1)
- **Pop:** O(1)
- **Peek:** O(1)
- **Space:** O(n)

---

# 6. Linear Queue

### Algorithm

```text
ENQUEUE(x)
1. If rear == size-1, display Overflow
2. Else if queue is empty, set front = 0
3. Increment rear and insert x

DEQUEUE()
1. If front == -1 or front > rear, display Underflow
2. Else remove queue[front] and increment front

DISPLAY()
1. If queue is empty, display Empty
2. Else print elements from front to rear
```

### Python Program

```python
size = int(input("Enter queue size: "))
queue = [0] * size
front = -1
rear = -1

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        if rear == size - 1:
            print("Queue Overflow")
        else:
            x = int(input("Enter element: "))

            if front == -1:
                front = 0

            rear += 1
            queue[rear] = x

    elif choice == 2:
        if front == -1 or front > rear:
            print("Queue Underflow")
        else:
            print("Deleted:", queue[front])
            front += 1

    elif choice == 3:
        if front == -1 or front > rear:
            print("Queue is empty")
        else:
            print("Queue:", end=" ")
            for i in range(front, rear + 1):
                print(queue[i], end=" ")
            print()

    elif choice == 4:
        break

    else:
        print("Invalid choice")
```

### Sample Output

```text
Enter queue size: 3

Enter choice: 1
Enter element: 10

Enter choice: 1
Enter element: 20

Enter choice: 3
Queue: 10 20

Enter choice: 2
Deleted: 10
```

### Complexity

- **Enqueue:** O(1)
- **Dequeue:** O(1)
- **Display:** O(n)
- **Space:** O(n)

---

# 7. Circular Queue

### Algorithm

```text
ENQUEUE(x)
1. If (rear + 1) % size == front, queue is full
2. Else if queue is empty, set front = rear = 0
3. Else rear = (rear + 1) % size
4. Insert x

DEQUEUE()
1. If front == -1, queue is empty
2. Remove queue[front]
3. If front == rear, set front = rear = -1
4. Else front = (front + 1) % size
```

### Python Program

```python
size = int(input("Enter queue size: "))
queue = [0] * size
front = -1
rear = -1

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        if (rear + 1) % size == front:
            print("Circular Queue Overflow")
        else:
            x = int(input("Enter element: "))

            if front == -1:
                front = 0
                rear = 0
            else:
                rear = (rear + 1) % size

            queue[rear] = x

    elif choice == 2:
        if front == -1:
            print("Circular Queue Underflow")
        else:
            print("Deleted:", queue[front])

            if front == rear:
                front = -1
                rear = -1
            else:
                front = (front + 1) % size

    elif choice == 3:
        if front == -1:
            print("Queue is empty")
        else:
            print("Queue:", end=" ")
            i = front

            while True:
                print(queue[i], end=" ")
                if i == rear:
                    break
                i = (i + 1) % size

            print()

    elif choice == 4:
        break

    else:
        print("Invalid choice")
```

### Sample Output

```text
Enter queue size: 3

Enter choice: 1
Enter element: 10

Enter choice: 1
Enter element: 20

Enter choice: 1
Enter element: 30

Enter choice: 2
Deleted: 10

Enter choice: 1
Enter element: 40

Enter choice: 3
Queue: 20 30 40
```

### Complexity

- **Enqueue:** O(1)
- **Dequeue:** O(1)
- **Display:** O(n)
- **Space:** O(n)

---

# 8. Infix to Prefix Using Stack

### Algorithm

```text
1. Reverse the infix expression.
2. Replace '(' with ')' and ')' with '('.
3. Convert the modified expression to postfix using a stack.
4. Reverse the postfix expression.
5. The result is prefix.
```

### Python Program

```python
def precedence(op):
    if op == '^':
        return 3
    elif op == '*' or op == '/':
        return 2
    elif op == '+' or op == '-':
        return 1
    return 0


def reverse_string(s):
    r = ""
    for i in range(len(s) - 1, -1, -1):
        r += s[i]
    return r


infix = input("Enter infix expression: ")
rev = reverse_string(infix)

temp = ""
for ch in rev:
    if ch == '(':
        temp += ')'
    elif ch == ')':
        temp += '('
    else:
        temp += ch

stack = []
postfix = ""

for ch in temp:
    if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z') or ('0' <= ch <= '9'):
        postfix += ch

    elif ch == '(':
        stack.append(ch)

    elif ch == ')':
        while stack and stack[-1] != '(':
            postfix += stack.pop()
        if stack:
            stack.pop()

    else:
        while stack and stack[-1] != '(' and precedence(stack[-1]) > precedence(ch):
            postfix += stack.pop()
        stack.append(ch)

while stack:
    postfix += stack.pop()

prefix = reverse_string(postfix)

print("Prefix expression:", prefix)
```

### Sample Output

```text
Enter infix expression: A+B*C
Prefix expression: +A*BC
```

### Complexity

- **Time:** O(n)
- **Space:** O(n)

---

# 9. Infix to Postfix Using Stack

### Algorithm

```text
1. Scan the infix expression from left to right.
2. If operand, add it to output.
3. If '(', push it.
4. If ')', pop until '(' is found.
5. For an operator, pop higher/equal precedence operators and push current operator.
6. Pop remaining operators.
```

### Python Program

```python
def precedence(op):
    if op == '^':
        return 3
    elif op == '*' or op == '/':
        return 2
    elif op == '+' or op == '-':
        return 1
    return 0


infix = input("Enter infix expression: ")

stack = []
postfix = ""

for ch in infix:
    if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z') or ('0' <= ch <= '9'):
        postfix += ch

    elif ch == '(':
        stack.append(ch)

    elif ch == ')':
        while stack and stack[-1] != '(':
            postfix += stack.pop()

        if stack:
            stack.pop()

    else:
        while stack and stack[-1] != '(' and precedence(stack[-1]) >= precedence(ch):
            postfix += stack.pop()

        stack.append(ch)

while stack:
    postfix += stack.pop()

print("Postfix expression:", postfix)
```

### Sample Output

```text
Enter infix expression: A+B*C
Postfix expression: ABC*+
```

### Complexity

- **Time:** O(n)
- **Space:** O(n)

---

# 10. Evaluate Prefix Expression Using Stack

### Algorithm

```text
1. Scan prefix expression from right to left.
2. If operand, push it onto stack.
3. If operator:
   a. Pop first operand.
   b. Pop second operand.
   c. Perform operation.
   d. Push result.
4. Final stack value is the answer.
```

### Python Program

```python
def operation(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b


def is_digit(ch):
    return '0' <= ch <= '9'


expr = input("Enter prefix expression: ")
stack = []

for i in range(len(expr) - 1, -1, -1):
    ch = expr[i]

    if is_digit(ch):
        stack.append(int(ch))
    else:
        a = stack.pop()
        b = stack.pop()
        stack.append(operation(a, b, ch))

print("Result:", stack[-1])
```

### Sample Output

```text
Enter prefix expression: -+7*45+20
Result: 25
```

### Complexity

- **Time:** O(n)
- **Space:** O(n)

---

# 11. Evaluate Postfix Expression Using Stack

### Algorithm

```text
1. Scan postfix expression from left to right.
2. If operand, push it.
3. If operator:
   a. Pop second operand.
   b. Pop first operand.
   c. Perform operation.
   d. Push result.
4. Final stack value is the answer.
```

### Python Program

```python
def operation(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b


def is_digit(ch):
    return '0' <= ch <= '9'


expr = input("Enter postfix expression: ")
stack = []

for ch in expr:
    if is_digit(ch):
        stack.append(int(ch))
    else:
        b = stack.pop()
        a = stack.pop()
        stack.append(operation(a, b, ch))

print("Result:", stack[-1])
```

### Sample Output

```text
Enter postfix expression: 745*+20-
Result: 27
```

### Complexity

- **Time:** O(n)
- **Space:** O(n)

---

# 12. Merge Sort

### Algorithm

```text
MergeSort(A, low, high)
1. If low < high:
2.    mid = (low + high) // 2
3.    Sort left half
4.    Sort right half
5.    Merge the two sorted halves
```

### Python Program

```python
def merge(a, low, mid, high):
    temp = []
    i = low
    j = mid + 1

    while i <= mid and j <= high:
        if a[i] <= a[j]:
            temp.append(a[i])
            i += 1
        else:
            temp.append(a[j])
            j += 1

    while i <= mid:
        temp.append(a[i])
        i += 1

    while j <= high:
        temp.append(a[j])
        j += 1

    k = 0
    for i in range(low, high + 1):
        a[i] = temp[k]
        k += 1


def merge_sort(a, low, high):
    if low < high:
        mid = (low + high) // 2

        merge_sort(a, low, mid)
        merge_sort(a, mid + 1, high)
        merge(a, low, mid, high)


n = int(input("Enter number of elements: "))
a = []

for i in range(n):
    a.append(int(input("Enter element: ")))

merge_sort(a, 0, n - 1)

print("Sorted array:", end=" ")
for i in range(n):
    print(a[i], end=" ")
```

### Sample Output

```text
Enter number of elements: 5
Enter element: 38
Enter element: 27
Enter element: 43
Enter element: 3
Enter element: 9
Sorted array: 3 9 27 38 43
```

### Complexity

- **Time:** O(n log n)
- **Space:** O(n)

---

# 13. Quick Sort

### Algorithm

```text
QuickSort(A, low, high)
1. If low < high:
2.    Choose a pivot.
3.    Partition array around pivot.
4.    Recursively sort left part.
5.    Recursively sort right part.
```

### Python Program

```python
def partition(a, low, high):
    pivot = a[high]
    i = low - 1

    for j in range(low, high):
        if a[j] <= pivot:
            i += 1

            temp = a[i]
            a[i] = a[j]
            a[j] = temp

    temp = a[i + 1]
    a[i + 1] = a[high]
    a[high] = temp

    return i + 1


def quick_sort(a, low, high):
    if low < high:
        p = partition(a, low, high)

        quick_sort(a, low, p - 1)
        quick_sort(a, p + 1, high)


n = int(input("Enter number of elements: "))
a = []

for i in range(n):
    a.append(int(input("Enter element: ")))

quick_sort(a, 0, n - 1)

print("Sorted array:", end=" ")
for i in range(n):
    print(a[i], end=" ")
```

### Sample Output

```text
Enter number of elements: 5
Enter element: 10
Enter element: 7
Enter element: 8
Enter element: 9
Enter element: 1
Sorted array: 1 7 8 9 10
```

### Complexity

- **Best/Average Time:** O(n log n)
- **Worst Time:** O(n²)
- **Space:** O(log n) average due to recursion
- **Worst Space:** O(n)

---

# 14. Matrix Chain Multiplication — Dynamic Programming

Given matrices A1, A2, ..., An, find the minimum number of scalar multiplications needed and the optimal parenthesization.

### Algorithm

```text
MatrixChain(p)
1. Let m[i][i] = 0.
2. For chain length L = 2 to n:
3.    For i = 1 to n-L+1:
4.       j = i + L - 1
5.       Set m[i][j] = infinity
6.       For k = i to j-1:
7.          cost = m[i][k] + m[k+1][j]
             + p[i-1] * p[k] * p[j]
8.          If cost is smaller:
             store cost and k
9. Use stored k values to print optimal parenthesization.
```

### Python Program

```python
def print_order(s, i, j):
    if i == j:
        print("A" + str(i), end="")
    else:
        print("(", end="")
        print_order(s, i, s[i][j])
        print_order(s, s[i][j] + 1, j)
        print(")", end="")


n = int(input("Enter number of matrices: "))

p = []
print("Enter matrix dimensions:")
print("For n matrices, enter n+1 dimensions.")

for i in range(n + 1):
    p.append(int(input("Dimension: ")))

m = []
s = []

for i in range(n + 1):
    m.append([0] * (n + 1))
    s.append([0] * (n + 1))

for length in range(2, n + 1):
    for i in range(1, n - length + 2):
        j = i + length - 1
        m[i][j] = 999999999

        for k in range(i, j):
            cost = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]

            if cost < m[i][j]:
                m[i][j] = cost
                s[i][j] = k

print("Minimum number of multiplications:", m[1][n])

print("Optimal parenthesization:", end=" ")
print_order(s, 1, n)
print()
```

### Sample Output

For matrices:

```text
A1 = 10 x 20
A2 = 20 x 30
A3 = 30 x 40
A4 = 40 x 30
```

Input:

```text
Enter number of matrices: 4
Enter matrix dimensions:
For n matrices, enter n+1 dimensions.
Dimension: 10
Dimension: 20
Dimension: 30
Dimension: 40
Dimension: 30
```

Output:

```text
Minimum number of multiplications: 30000
Optimal parenthesization: (((A1A2)A3)A4)
```

### Complexity

- **Time:** O(n³)
- **Space:** O(n²)

---

# Quick Complexity Revision Table

| No. | Algorithm / Operation | Time Complexity | Space Complexity |
|---|---|---|---|
| 1 | Binary Search | O(log n) | O(1) |
| 2 | Bitonic Point | O(log n) | O(1) |
| 3 | Selection Sort | O(n²) | O(1) |
| 4 | Optimized Bubble Sort | Best O(n), Worst O(n²) | O(1) |
| 5 | Stack Push/Pop/Peek | O(1) | O(n) |
| 6 | Linear Queue | O(1) operation | O(n) |
| 7 | Circular Queue | O(1) operation | O(n) |
| 8 | Infix → Prefix | O(n) | O(n) |
| 9 | Infix → Postfix | O(n) | O(n) |
| 10 | Prefix Evaluation | O(n) | O(n) |
| 11 | Postfix Evaluation | O(n) | O(n) |
| 12 | Merge Sort | O(n log n) | O(n) |
| 13 | Quick Sort | Avg O(n log n), Worst O(n²) | Avg O(log n) |
| 14 | Matrix Chain Multiplication | O(n³) | O(n²) |

---

# Important Exam Points

### Searching
- Binary Search requires a **sorted sequence**.
- Binary Search repeatedly divides the search space into two halves.

### Sorting
- Selection Sort selects the minimum element in every pass.
- Optimized Bubble Sort stops if a complete pass makes no swaps.
- Merge Sort uses **divide and conquer**.
- Quick Sort uses **divide and conquer** and a pivot.

### Stack
- Stack follows **LIFO** — Last In, First Out.
- Push inserts an element.
- Pop removes the top element.
- Peek returns the top element without removing it.

### Queue
- Queue follows **FIFO** — First In, First Out.
- Enqueue inserts at rear.
- Dequeue removes from front.
- Circular Queue reuses empty positions using modulo operation.

### Expression Conversion
- **Infix:** `A+B`
- **Prefix:** `+AB`
- **Postfix:** `AB+`

### Dynamic Programming
- Matrix Chain Multiplication does not change the order of matrices.
- It finds the parenthesization requiring the minimum scalar multiplications.
