# Stack & Queue Applications

## 1. Sliding Window Maximum

Need the maximum of every window of size `k`.

### Pattern

```text
Monotonic Deque
```

Maintain useful candidates in decreasing order.

Remove:

```text
1. Elements outside the window
2. Elements smaller than the current element
```

---

## 2. Stock Span

For each day:

```text
How many consecutive previous days
have price <= today's price?
```

### Pattern

```text
Previous Greater Element
+
Monotonic Stack
```

---

## 3. Celebrity Problem

Celebrity condition:

```text
Everyone knows celebrity
Celebrity knows nobody
```

### Pattern

```text
Elimination
+
Verification
```

Instead of checking every person against everyone:

```text
Eliminate impossible candidates
        ↓
Verify final candidate
```

---

## 4. LRU Cache

LRU = **Least Recently Used**

Required operations:

```text
get()
put()
```

Target:

```text
O(1)
```

### Core structure

```text
HashMap
+
Doubly Linked List
```

HashMap:

```text
key → node
```

Doubly linked list:

```text
Most Recently Used
        ↓
...
        ↓
Least Recently Used
```

---

## 5. LFU Cache

LFU = **Least Frequently Used**

Required operations:

```text
get()
put()
```

Core idea:

```text
HashMap
+
Frequency tracking
+
Doubly Linked Lists
```

When frequencies tie, recency is used to decide which item to remove.

---

## Problems

1. Sliding Window Maximum
2. Stock Span
3. Celebrity Problem
4. LRU Cache
5. LFU Cache

---

## Key Takeaway

```text
Sliding Window Maximum
→ Monotonic Deque

Stock Span
→ Previous Greater

Celebrity
→ Elimination + Verification

LRU
→ HashMap + DLL

LFU
→ HashMap + Frequency + DLL
```
