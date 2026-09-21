# STACK & QUEUE — PATTERN CHEATSHEET

## Core Data Structures

| Need                   | Think                 |
| ---------------------- | --------------------- |
| LIFO                   | Stack                 |
| FIFO                   | Queue                 |
| Both ends              | Deque                 |
| Ordered candidates     | Monotonic Stack/Deque |
| O(1) lookup + ordering | HashMap + Linked List |

---

## Monotonic Stack

| Problem Type     | Pattern                    |
| ---------------- | -------------------------- |
| Next Greater     | Monotonic decreasing stack |
| Next Smaller     | Monotonic increasing stack |
| Previous Greater | Monotonic stack            |
| Previous Smaller | Monotonic stack            |
| Circular NGE     | 2N traversal / modulo      |
| Stock Span       | Previous Greater           |
| Histogram        | Previous + Next Smaller    |

---

## Contribution

```text
Element's contribution
=
number of valid choices on left
×
number of valid choices on right
×
element value
```

Used for:

```text
Sum of Subarray Minimums
Sum of Subarray Ranges
```

---

## Histogram

```text
Previous Smaller
        +
Next Smaller
        ↓
Maximum Width
        ↓
height × width
```

---

## Matrix → Histogram

```text
Each row
   ↓
Build heights
   ↓
Largest Rectangle in Histogram
   ↓
Maximal Rectangle
```

---

## Monotonic Deque

```text
Sliding Window Maximum
```

Maintain:

```text
indices
+
decreasing values
```

Remove:

```text
out-of-window indices
+
dominated smaller values
```

---

## Greedy Stack

```text
Remove K Digits
```

Rule:

```text
while current < stack[-1]
and k > 0:
    remove stack[-1]
```

---

## Simulation

```text
Asteroid Collision
```

Stack stores surviving elements.

---

## Cache Patterns

### LRU

```text
HashMap + Doubly Linked List
```

### LFU

```text
HashMap
+
Frequency Map
+
Doubly Linked Lists
```

---

## Fast Recognition

```text
"next greater"
        → Monotonic Stack

"next smaller"
        → Monotonic Stack

"previous greater/smaller"
        → Monotonic Stack

"span"
        → Previous Greater

"subarray minimum/maximum contribution"
        → Monotonic Stack

"largest rectangle"
        → Previous/Next Smaller

"sliding window maximum"
        → Monotonic Deque

"remove digits to minimize"
        → Greedy Monotonic Stack

"least recently used"
        → HashMap + DLL

"least frequently used"
        → HashMap + Frequency + DLL
```

---

## Golden Rule

> **Don't memorize the problem. Recognize the pattern.**
