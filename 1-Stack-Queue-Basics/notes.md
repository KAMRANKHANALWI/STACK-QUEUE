# Stack & Queue Basics

## 1. Stack

**LIFO — Last In, First Out**

```text
push()
pop()
peek() / top()
is_empty()
```

Typical implementation:

```text
Array / List
Linked List
```

### Core idea

All insertions and removals happen from the **same end**.

---

## 2. Queue

**FIFO — First In, First Out**

```text
enqueue()
dequeue()
front()
is_empty()
```

Typical implementation:

```text
Array
Linked List
```

### Core idea

Insertion happens at the **rear** and removal at the **front**.

---

## 3. Stack ↔ Queue

Important implementation exercises:

```text
Stack using Queue
Queue using Stack
```

The goal is to understand how changing the order of operations can simulate the behavior of another data structure.

---

## 4. Balanced Parentheses

### Pattern

```text
Opening bracket → push
Closing bracket → match with stack top
```

Valid only when:

```text
Every closing bracket matches
+
No unmatched opening brackets remain
```

---

## 5. Min Stack

Requirement:

```text
push()
pop()
top()
getMin()
```

Target:

```text
O(1) getMin()
```

Core idea:

> Store enough information to know the minimum without scanning the stack.

---

## Problems

1. Implement Stack using Array
2. Implement Queue using Array
3. Implement Stack using Queue
4. Implement Queue using Stack
5. Implement Stack using Linked List
6. Implement Queue using Linked List
7. Balanced Parentheses
8. Implement Min Stack

---

## Key Takeaway

```text
Stack → LIFO
Queue → FIFO

Matching / nesting → Stack

Need minimum while supporting stack operations
→ Min Stack pattern
```
