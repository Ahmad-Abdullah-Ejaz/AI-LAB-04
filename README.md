# AI-LAB-04
# Artificial Intelligence Lab 04: Fundamental Data Structures & Search Algorithms

This repository contains Python implementations for **Lab 04** of the Artificial Intelligence course. The lab focuses on fundamental linear data structures (Stack and Queue) and the divide-and-conquer Binary Search algorithm.

---

## 📁 Repository Structure

```text
.
├── Stack.py             # Task 1: Stack implementation using Python list (LIFO)
├── Queue.py             # Task 2: Queue implementation using collections.deque (FIFO)
├── binarySearch_01.py   # Task 3: Interactive Binary Search accepting dynamic user input
├── binarySearch_02.py   # Task 3: Step-by-step trace demonstration of Binary Search
└── README.md            # Lab documentation
```

---

## 📌 Tasks Overview

### Task 1: Stack Implementation (`Stack.py`)
A Stack is a linear data structure that operates under the **LIFO** (Last In, First Out) principle.
* **Core Operations:**
  * `push(item)`: Adds an element to the top of the stack.
  * `pop()`: Removes and returns the top element (handles underflow when empty).
  * `peek()`: Returns the top element without removing it.
  * `is_empty()`: Returns `True` if the stack contains no elements, otherwise `False`.
  * `size()`: Returns the total number of elements in the stack.
  * `display()`: Outputs the current elements in the stack.

### Task 2: Queue Implementation (`Queue.py`)
A Queue is a linear data structure that operates under the **FIFO** (First In, First Out) principle. This implementation leverages Python's built-in `collections.deque` for optimized $O(1)$ appends and pops from both ends.
* **Core Operations:**
  * `enqueue(item)`: Inserts an element at the rear of the queue.
  * `dequeue()`: Removes and returns the front element (handles underflow).
  * `front()`: Returns the front element without dequeuing.
  * `is_empty()`: Checks whether the queue is empty.
  * `size()`: Returns current queue length.
  * `display()`: Outputs all queued elements.

### Task 3: Binary Search (`binarySearch_01.py` & `binarySearch_02.py`)
Binary Search is a dichotomous divide-and-conquer algorithm designed for sorted lists. It recursively or iteratively halves the search space by evaluating the median element:

$$mid = \left\lfloor\frac{low + high}{2}\right\rfloor$$

* If `arr[mid] == target`: Element found; index returned.
* If `arr[mid] < target`: Target is in the right subarray $\rightarrow$ `low = mid + 1`.
* If `arr[mid] > target`: Target is in the left subarray $\rightarrow$ `high = mid - 1`.

#### Scripts Included:
* **`binarySearch_01.py`**: Accepts dynamic array input and target values directly from the user.
* **`binarySearch_02.py`**: Traces execution step-by-step in a structured tabular output (`Step`, `Low`, `High`, `Mid`, `Value`, `Action`).

---

## ⏱️ Complexity Analysis

| Data Structure / Algorithm | Operation / Case | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Stack** | Push / Pop / Peek | $O(1)$ | $O(n)$ |
| **Queue** (`deque`) | Enqueue / Dequeue / Front | $O(1)$ | $O(n)$ |
| **Binary Search** | Best Case | $O(1)$ | $O(1)$ |
| **Binary Search** | Average / Worst Case | $O(\log n)$ | $O(1)$ |

---

## 🚀 Running the Code

Ensure Python 3 is installed, then run each script from your terminal:

```bash
# Task 1: Stack
python Stack.py

# Task 2: Queue
python Queue.py

# Task 3: Binary Search (Dynamic input)
python binarySearch_01.py

# Task 3: Binary Search (Step trace output)
python binarySearch_02.py
```
