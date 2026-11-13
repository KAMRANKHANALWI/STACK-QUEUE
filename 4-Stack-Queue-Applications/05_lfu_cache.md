# 05. LFU Cache

## Problem

**LeetCode 460 — LFU Cache**

Design a data structure that supports two operations in O(1) average time:

- `get(key)` → Return the value if the key exists; otherwise return `-1`.
- `put(key, value)` → Insert or update a key-value pair.

Eviction rules:

1. Remove the **Least Frequently Used (LFU)** key.
2. If multiple keys have the same frequency, remove the **Least Recently Used (LRU)** key among them.

---

## Pattern

**Hash Maps + Doubly Linked Lists**

### Key Observation

We need to track two things:

1. Frequency → How many times has a key been accessed?
2. Recency → Among keys with equal frequency, which was used least recently?

We use Hash Maps for direct access and Doubly Linked Lists to maintain recency.

---

## 1. Data Structures

| Data Structure | Responsibility |
|---|---|
| `key_to_node` | Maps key → Node |
| `freq_to_dll` | Maps frequency → Doubly Linked List |
| `min_freq` | Tracks minimum frequency currently present |
| `capacity` | Maximum cache size |
| `size` | Current number of elements |

### Node Structure

Each node stores:

```python
key
value
freq
prev
next
```

Every new node starts with:

```python
self.freq = 1
```

### Doubly Linked List

Each frequency has its own DLL.

```text
Frequency 1:

HEAD ⇄ Node ⇄ Node ⇄ TAIL

Frequency 2:

HEAD ⇄ Node ⇄ TAIL

Frequency 3:

HEAD ⇄ Node ⇄ Node ⇄ TAIL
```

Within each frequency list:

- Front → Most Recently Used (MRU).
- Back → Least Recently Used (LRU).

This allows us to resolve frequency ties in O(1).

---

## 2. Core Intuition

LFU is essentially multiple LRU lists grouped by frequency.

Example:

```text
Frequency 1:
HEAD ⇄ A ⇄ B ⇄ TAIL

Frequency 2:
HEAD ⇄ C ⇄ D ⇄ TAIL

Frequency 3:
HEAD ⇄ E ⇄ TAIL
```

If eviction is required:

1. Find the minimum frequency using `min_freq`.
2. Access that frequency's DLL.
3. Remove the node at the back.

```python
dll = self.freq_to_dll[self.min_freq]

node = dll.remove_lru()
```

The minimum frequency determines which list to use. The DLL determines which key to evict within that frequency.

---

## 3. Doubly Linked List Operations

We use three operations inside the DLL.

### A. insert_front(node)

Insert a node immediately after HEAD.

```text
Before:

HEAD ⇄ A ⇄ B ⇄ TAIL

Insert X:

HEAD ⇄ X ⇄ A ⇄ B ⇄ TAIL
```

The new node becomes the most recently used node in that frequency.

### B. remove(node)

Remove a given node from its current position.

```text
Before:

A ⇄ B ⇄ C

Remove B:

A ⇄ C
```

We already have the node reference, so no traversal is required.

### C. remove_lru()

Remove the node immediately before TAIL.

```text
HEAD ⇄ A ⇄ B ⇄ C ⇄ TAIL
                         ↑
                        LRU

Remove C:

HEAD ⇄ A ⇄ B ⇄ TAIL
```

This handles the LRU tie-breaking rule.

All three operations take O(1) time.

---

## 4. The Most Important Operation — update_freq()

Whenever an existing key is accessed successfully, its frequency increases.

Suppose a node currently has frequency 2.

```text
Step 1:
Remove node from frequency 2 DLL.

Step 2:
Increase its frequency to 3.

Step 3:
Insert it at the front of frequency 3 DLL.
```

Visual:

```text
Before:

Frequency 2: HEAD ⇄ A ⇄ B ⇄ TAIL

Frequency 3: HEAD ⇄ C ⇄ TAIL

Access B:

Frequency 2: HEAD ⇄ A ⇄ TAIL

Frequency 3: HEAD ⇄ B ⇄ C ⇄ TAIL
```

Pseudocode:

```text
freq = node.freq

dll = freq_to_dll[freq]

remove node from current DLL

if DLL becomes empty and freq == min_freq:
    min_freq += 1

node.freq += 1

new_freq = node.freq

if new_freq DLL does not exist:
    create DLL

insert node at front of new_freq DLL
```

### Understanding min_freq

`min_freq` stores the minimum frequency currently present in the cache.

Example:

```text
Frequency 1: Empty

Frequency 2: A ⇄ B

Frequency 3: C

min_freq = 2
```

If the last node in frequency 2 moves to frequency 3:

```python
if dll.size == 0 and self.min_freq == freq:
    self.min_freq += 1
```

The minimum frequency becomes 3.

**Important:** The accessed node itself moves to the next frequency, so that next frequency list is guaranteed to contain at least that node.

---

## 5. Core Operations

### A. get(key)

Logic:

1. Check whether the key exists in `key_to_node`.
2. If absent, return `-1`.
3. Retrieve the node.
4. Increase its frequency using `update_freq()`.
5. Return its value.

Pseudocode:

```text
if key does not exist:
    return -1

node = key_to_node[key]

update_freq(node)

return node.value
```

Every successful `get()` increases frequency by one.

### B. put(key, value)

There are three cases.

**Case 1: Capacity is zero**

```text
if capacity == 0:
    return
```

No element can be stored.

**Case 2: Key already exists**

```text
node = key_to_node[key]

node.value = value

update_freq(node)

return
```

- Retrieve the existing node.
- Update its value.
- Increase its frequency.
- Move it to the front of the next frequency DLL.

Updating an existing key also increases frequency.

**Case 3: New key**

```text
if cache is full:

    dll = freq_to_dll[min_freq]

    node = dll.remove_lru()

    delete node.key from key_to_node

    size -= 1

node = new Node(key, value)

min_freq = 1

if frequency 1 DLL does not exist:
    create DLL

insert node into frequency 1 DLL

key_to_node[key] = node

size += 1
```

Important observations:

- Every new key starts at frequency 1.
- If the cache is full, evict the LRU node from the minimum-frequency DLL.
- After inserting a new key, reset `min_freq = 1`.

---

## 6. Dry Run 

Capacity = 3

Operations:

```python
put(1, 10)
put(2, 20)
put(3, 30)
put(4, 40)

get(3)
get(2)
get(4)

put(5, 50)
put(2, 25)
```

| Operation | Result | Cache (key:frequency) |
|---|---|---|
| `put(1,10)` | Insert | `1:1` |
| `put(2,20)` | Insert | `2:1, 1:1` |
| `put(3,30)` | Insert | `3:1, 2:1, 1:1` |
| `put(4,40)` | Evict key 1 | `4:1, 3:1, 2:1` |
| `get(3)` | Returns 30 | `3:2, 4:1, 2:1` |
| `get(2)` | Returns 20 | `2:2, 3:2, 4:1` |
| `get(4)` | Returns 40 | `4:2, 2:2, 3:2` |
| `put(5,50)` | Evict key 3 | `5:1, 4:2, 2:2` |
| `put(2,25)` | Update value; frequency increases | `5:1, 2:3, 4:2` |

### Important observations

**Step 4: `put(4,40)`**

All existing keys have frequency 1.

```text
Frequency 1:

HEAD ⇄ 3 ⇄ 2 ⇄ 1 ⇄ TAIL
                      ↑
                     LRU
```

Key 1 is evicted.

**Step 8: `put(5,50)`**

Keys 2, 3 and 4 all have frequency 2.

```text
Frequency 2:

HEAD ⇄ 4 ⇄ 2 ⇄ 3 ⇄ TAIL
                      ↑
                     LRU
```

Key 3 is evicted.

**Step 9: `put(2,25)`**

Key 2 already exists.

- Update its value from 20 to 25.
- Increase frequency from 2 to 3.
- Move it into frequency 3 DLL.

No eviction is needed.

---

## 7. Overall Algorithm Flow

### GET(key)

```text
       Is key present?
          /     \
        No       Yes
        |         |
     Return -1  Get node
                  |
             Update frequency
                  |
             Return value
```

### PUT(key, value)

```text
          Capacity = 0?
           /       \
         Yes        No
          |          |
        Return   Does key exist?
                  /       \
                Yes        No
                 |          |
             Get node    Is cache full?
                 |          |
            Update value   Yes → Evict LRU
                 |          |   from min_freq DLL
            Update freq    |
                 |       Create new node
               Return       |
                         Set min_freq = 1
                             |
                         Insert at front
                             |
                         Update Hash Map
```

---

## 8. Complexity Analysis

| Operation | Complexity |
|---|---|
| Hash Map lookup | O(1) average |
| Insert into DLL | O(1) |
| Remove from DLL | O(1) |
| Remove LRU node | O(1) |
| Frequency update | O(1) |
| `get()` | O(1) average |
| `put()` | O(1) average |
| Space | O(capacity) |

Why O(1)?

- Hash Maps provide O(1) average lookup.
- DLL operations use direct node references.
- `min_freq` avoids searching for the minimum frequency.
- No linked-list traversal is required.

---

## 9. Important Interview Takeaways

1. Every new node starts with `freq = 1`.
2. Every successful `get()` increases frequency.
3. Updating an existing key through `put()` also increases frequency.
4. Each frequency maintains its own DLL.
5. The front of each DLL is MRU; the back is LRU.
6. `min_freq` tracks the minimum frequency currently present.
7. When the minimum-frequency DLL becomes empty, update `min_freq`.
8. When inserting a new key, reset `min_freq = 1`.

---

## 10. Key Takeaway

```text
LFU Cache
    |
    ├── key_to_node
    |      └── Find node using key
    |
    ├── freq_to_dll
    |      └── Maintain recency within each frequency
    |
    └── min_freq
           └── Identify the eviction frequency
```

Central pattern:

```text
Find node
    ↓
Remove from current frequency DLL
    ↓
Increase frequency
    ↓
Insert into next frequency DLL
```

**Remember:**

LFU = Frequency first, Recency second.

The combination of Hash Maps, Doubly Linked Lists and `min_freq` allows both `get()` and `put()` to run in O(1) average time.
