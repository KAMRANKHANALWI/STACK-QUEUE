# Stack & Queue Patterns

The purpose of this section is to connect individual problems into reusable patterns.

---

## Pattern 1 — LIFO

```text
Stack
```

Use when the most recently processed element matters first.

Examples:

```text
Balanced Parentheses
Expression Conversion
Simulation
```

---

## Pattern 2 — FIFO

```text
Queue
```

Use when elements must be processed in arrival order.

---

## Pattern 3 — Monotonic Stack

Use when looking for:

```text
Next Greater
Next Smaller
Previous Greater
Previous Smaller
```

---

## Pattern 4 — Contribution

Instead of examining every subarray:

```text
Count how many subarrays
an element contributes to.
```

Used in:

```text
Sum of Subarray Minimums
Sum of Subarray Ranges
```

---

## Pattern 5 — Boundary

Find:

```text
Previous boundary
+
Next boundary
```

Used heavily in:

```text
Largest Rectangle in Histogram
```

---

## Pattern 6 — Monotonic Deque

Used when a sliding window needs an extreme value efficiently.

```text
Sliding Window Maximum
```

---

## Pattern 7 — Greedy Stack

Use a stack to remove elements that are locally worse.

Example:

```text
Remove K Digits
```

---

## Pattern 8 — HashMap + Linked List

Used when we need:

```text
O(1) lookup
+
O(1) ordering updates
```

Examples:

```text
LRU Cache
LFU Cache
```

---

## Pattern Recognition Questions

When seeing a Stack/Queue problem, ask:

```text
1. Is this LIFO?
2. Is this FIFO?
3. Do I need matching/nesting?
4. Do I need next/previous greater?
5. Do I need next/previous smaller?
6. Do I need contribution counts?
7. Do I need boundaries?
8. Is this a sliding window?
9. Do I need a monotonic deque?
10. Do I need O(1) lookup + ordering?
```

---

## Final Mental Model

```text
STACK
 ├── LIFO
 ├── Matching
 ├── Expressions
 ├── Simulation
 └── Monotonic Stack
       ├── Greater
       ├── Smaller
       ├── Contribution
       └── Boundaries

QUEUE
 ├── FIFO
 └── Deque
       └── Sliding Window

CACHE
 ├── HashMap
 └── Linked List
       ├── LRU
       └── LFU
```
