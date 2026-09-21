# STACK & QUEUE

A structured collection of **Stack & Queue** problems from the **Striver A2Z DSA Sheet + TUF YouTube playlist**, implemented in Python.

The goal is not just to solve problems, but to recognize the underlying **Stack, Queue, Monotonic Stack, Monotonic Queue, and Cache patterns**.

---

## 📚 Roadmap

```text
1. Stack & Queue Basics
        ↓
2. Expression Conversion
        ↓
3. Monotonic Stack
        ↓
4. Stack & Queue Applications
        ↓
5. Stack & Queue Patterns
```

---

## 📂 Repository Structure

```text
STACK-QUEUE/
│
├── README.md
│
├── 1-Stack-Queue-Basics/
│   ├── 01_implement_stack_using_array.py
│   ├── 02_implement_queue_using_array.py
│   ├── 03_implement_stack_using_queue.py
│   ├── 04_implement_queue_using_stack.py
│   ├── 05_implement_stack_using_linked_list.py
│   ├── 06_implement_queue_using_linked_list.py
│   ├── 07_balanced_parentheses.py
│   ├── 08_min_stack.py
│   └── notes.md
│
├── 2-Expression-Conversion/
│   ├── 01_infix_to_postfix.py
│   ├── 02_prefix_to_infix.py
│   ├── 03_prefix_to_postfix.py
│   ├── 04_postfix_to_prefix.py
│   ├── 05_postfix_to_infix.py
│   ├── 06_infix_to_prefix.py
│   └── notes.md
│
├── 3-Monotonic-Stack/
│   ├── 01_next_greater_element.py
│   ├── 02_next_greater_element_ii.py
│   ├── 03_next_smaller_element.py
│   ├── 04_number_of_greater_elements_to_right.py
│   ├── 05_trapping_rainwater.py
│   ├── 06_sum_of_subarray_minimums.py
│   ├── 07_asteroid_collision.py
│   ├── 08_sum_of_subarray_ranges.py
│   ├── 09_remove_k_digits.py
│   ├── 10_largest_rectangle_in_histogram.py
│   ├── 11_maximal_rectangle.py
│   └── notes.md
│
├── 4-Stack-Queue-Applications/
│   ├── 01_sliding_window_maximum.py
│   ├── 02_stock_span.py
│   ├── 03_celebrity_problem.py
│   ├── 04_lru_cache.py
│   ├── 05_lfu_cache.py
│   └── notes.md
│
└── 5-Stack-Queue-Patterns/
    ├── pattern-cheatsheet.md
    └── notes.md
```

---

## 🧩 Core Concepts

### Stack

**LIFO — Last In, First Out**

```text
push → add to top
pop  → remove from top
peek → access top
```

Common uses:

* Matching parentheses
* Expression conversion
* Previous/Next Greater or Smaller
* Simulation
* Greedy problems

---

### Queue

**FIFO — First In, First Out**

```text
enqueue → add at rear
dequeue → remove from front
front   → access first element
```

Common uses:

* FIFO processing
* Sliding windows
* BFS-related problems
* Scheduling

---

### Monotonic Stack

A stack maintained in a specific increasing/decreasing order.

Main applications:

```text
Next Greater Element
Next Smaller Element
Previous Greater Element
Previous Smaller Element
Stock Span
Histogram
Subarray Minimums
Subarray Ranges
```

---

### Monotonic Queue

A deque maintained so that useful candidates remain ordered.

Main application:

```text
Sliding Window Maximum
```

---

## 🎯 Learning Philosophy

For every problem, focus on:

```text
Problem
    ↓
Pattern
    ↓
Key Observation
    ↓
Approach
    ↓
Dry Run
    ↓
Complexity
    ↓
Takeaway
```

The individual `.py` files intentionally keep explanations concise and focused on reconstructing the solution.

---

## 🔥 Important Pattern Connections

```text
Next Greater
     ↓
Monotonic Stack
     ↓
Stock Span

Previous / Next Smaller
     ↓
Contribution Technique
     ↓
Subarray Minimums

Previous Smaller + Next Smaller
     ↓
Largest Rectangle
     ↓
Maximal Rectangle

Monotonic Stack
     ↓
Sliding Window
     ↓
Monotonic Queue

HashMap + Doubly Linked List
     ↓
LRU Cache

HashMap + Frequency + Doubly Linked List
     ↓
LFU Cache
```

---

## 📊 Problem Count

| Section                    | Problems |
| -------------------------- | -------: |
| Stack & Queue Basics       |        8 |
| Expression Conversion      |        6 |
| Monotonic Stack            |       11 |
| Stack & Queue Applications |        5 |
| **Total**                  |   **30** |

---

## 🛠 Language

**Python 3**

---

## 🎯 Final Goal

By the end of this repository, the objective is to recognize:

> **"What Stack/Queue pattern is hiding behind this problem?"**

rather than memorizing individual solutions.
