# 04. LRU Cache

## Problem

**LeetCode 146 — LRU Cache**

Design a data structure that follows the Least Recently Used (LRU) cache eviction policy.

Implement the `LRUCache` class:

- `LRUCache(capacity)` → Initialize the cache with a positive capacity.
- `get(key)` → Return the value if the key exists; otherwise return `-1`.
- `put(key, value)` → Insert or update a key-value pair.
- If the cache exceeds its capacity, evict the least recently used key.

Both `get()` and `put()` must run in **O(1) average time**.

---

## Pattern

**Hash Map + Doubly Linked List**

### Key Observation

We need two things:

1. Fast lookup of a key.
2. Fast insertion, deletion and movement of any node.

A single data structure cannot efficiently handle both requirements.

| Data Structure | Responsibility |
|---|---|
| Hash Map | Find a node using its key in O(1) average |
| Doubly Linked List | Insert, delete and move nodes in O(1) |

---

## 1. Understanding LRU

LRU = **Least Recently Used**.

When the cache is full and a new key is inserted, remove the key that has not been accessed for the longest time.

Example:

```text
Capacity = 2

put(1, 10)
put(2, 20)

HEAD → 2 → 1 → TAIL
        MRU   LRU

get(1)

HEAD → 1 → 2 → TAIL
        MRU   LRU

put(3, 30)

HEAD → 3 → 1 → TAIL
        MRU   LRU

Evicted key = 2
```

Every successful `get()` and every `put()` makes that key the most recently used.

---

## 2. Data Structures

### A. Hash Map

```python
self.cache = {}
```

Stores:

```text
key → Node reference
```

Example:

```text
{
    1: address(Node1),
    2: address(Node2),
    3: address(Node3)
}
```

**Why?**

- Direct access to a node using its key.
- O(1) average lookup.
- No linked-list traversal is needed.

### B. Doubly Linked List

Each node contains:

```python
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

        self.prev = None
        self.next = None
```

**Why Doubly Linked List?**

- Insert at the front in O(1).
- Delete any node in O(1), given its reference.
- Move an accessed node to the front in O(1).

We store both `key` and `value` because eviction requires the key to remove the corresponding entry from the Hash Map.

---

## 3. Dummy Head and Tail

We maintain two dummy nodes:

```text
HEAD ⇄ TAIL
```

Initially, both are connected.

Complete structure:

```text
NULL ← HEAD ⇄ Node1 ⇄ Node2 ⇄ TAIL → NULL
```

Rules:

- `head.next` → Most Recently Used (MRU).
- `tail.prev` → Least Recently Used (LRU).
- Insert new or accessed nodes immediately after HEAD.
- Evict the node immediately before TAIL.

**Why dummy nodes?**

They simplify insertion and deletion because we don't need separate handling for the first and last actual nodes.

---

## 4. Helper Functions

These two functions are the backbone of the implementation.

### A. remove(node)

Purpose: Remove a node from its current position.

```python
def remove(self, node):
    prev_node = node.prev
    next_node = node.next

    prev_node.next = next_node
    next_node.prev = prev_node
```

Visual:

```text
Before:

A ⇄ B ⇄ C

Remove B:

A ⇄ C
```

We don't need to traverse the list because we already have the node reference.

### B. insert_after_head(node)

Purpose: Insert a node immediately after the dummy HEAD.

```python
def insert_after_head(self, node):
    curr_after_head = self.head.next

    self.head.next = node
    node.prev = self.head

    node.next = curr_after_head
    curr_after_head.prev = node
```

Visual:

```text
Before:

HEAD ⇄ A ⇄ B ⇄ TAIL

Insert X:

HEAD ⇄ X ⇄ A ⇄ B ⇄ TAIL
```

**Pointer update order:**

1. Save the current node after HEAD.
2. Connect HEAD to the new node.
3. Connect the new node back to HEAD.
4. Connect the new node to the previous first node.
5. Connect the previous first node back to the new node.

Both helper functions take O(1) time.

---

## 5. Core Operations

### A. get(key)

Logic:

1. Check whether the key exists in the map.
2. If absent, return `-1`.
3. Retrieve the node from the map.
4. Save its value.
5. Remove the node from its current position.
6. Insert the same node immediately after HEAD.
7. Return its value.

Pseudocode:

```text
if key does not exist:
    return -1

node = map[key]
value = node.value

remove(node)
insert_after_head(node)

return value
```

**Important:** We reuse the existing node. We don't create a new node during `get()`.

### B. put(key, value)

There are two main cases.

**Case 1: Key already exists**

```text
node = map[key]

update node.value

remove(node)
insert_after_head(node)
```

- Retrieve the existing node.
- Update its value.
- Move it to the front.
- No map update is required because the map already points to the same node.

**Case 2: Key does not exist**

```text
if cache is full:

    node = tail.prev

    delete node.key from map
    remove(node)

node = new Node(key, value)

map[key] = node

insert_after_head(node)
```

Steps:

1. Check whether the cache is full.
2. If full, get `tail.prev`.
3. This is the LRU node.
4. Remove its key from the map.
5. Remove it from the linked list.
6. Create a new node.
7. Add its reference to the map.
8. Insert it after HEAD.

**Important distinction:**

Updating an existing key does not require eviction. Eviction is needed only when inserting a new key into a full cache.

---

## 6. Complete Algorithm Flow

### GET(key)

```text
          Is key present?
             /     \
           No       Yes
           |         |
        Return -1  Get node
                     |
                  Save value
                     |
                 Remove node
                     |
               Insert after HEAD
                     |
                 Return value
```

### PUT(key, value)

```text
          Does key exist?
             /     \
           Yes      No
           |         |
       Get node    Is cache full?
           |         |
      Update value  Yes → Remove TAIL.prev
           |              |
       Remove node    Remove from map
           |              |
       Insert at front  Remove from list
                          |
                      Create node
                          |
                      Update map
                          |
                    Insert at front
```

---

## 7. Dry Run

Capacity = 4

Operations:

```python
put(2, 6)
put(4, 7)
put(8, 11)
put(7, 10)
get(2)
get(8)
put(5, 6)
get(7)
put(5, 7)
```

Convention:

```text
LEFT = MRU
RIGHT = LRU
```

| Step | Operation | Returned Value | Cache: MRU → LRU |
|---|---|---:|---|
| 1 | `put(2, 6)` | — | 2 |
| 2 | `put(4, 7)` | — | 4 → 2 |
| 3 | `put(8, 11)` | — | 8 → 4 → 2 |
| 4 | `put(7, 10)` | — | 7 → 8 → 4 → 2 |
| 5 | `get(2)` | 6 | 2 → 7 → 8 → 4 |
| 6 | `get(8)` | 11 | 8 → 2 → 7 → 4 |
| 7 | `put(5, 6)` | — | 5 → 8 → 2 → 7 |
| 8 | `get(7)` | 10 | 7 → 5 → 8 → 2 |
| 9 | `put(5, 7)` | — | 5 → 7 → 8 → 2 |

### Important observations

**Step 7: `put(5, 6)`**

The cache is full.

```text
Before:

HEAD → 8 → 2 → 7 → 4 → TAIL
                              ↑
                             LRU
```

Evict key `4`.

Insert key `5` at the front:

```text
HEAD → 5 → 8 → 2 → 7 → TAIL
```

**Step 9: `put(5, 7)`**

Key `5` already exists.

- Update its value from `6` to `7`.
- Move the same node to the front.
- No eviction is required.

Final cache:

```text
HEAD
  |
  v
[5, 7] ⇄ [7, 10] ⇄ [8, 11] ⇄ [2, 6]
                                      |
                                      v
                                     TAIL
```

Evicted key: `4`

---

## 8. Time and Space Complexity

| Operation | Complexity | Reason |
|---|---|---|
| Map lookup | O(1) average | Hash Map |
| `remove(node)` | O(1) | Direct pointer access |
| `insert_after_head()` | O(1) | Direct pointer updates |
| `get()` | O(1) average | No traversal |
| `put()` | O(1) average | No traversal |
| Space | O(capacity) | Map + linked list |

The O(1) average lookup assumption comes from using a Hash Map.

---

## 9. Important Concepts to Remember

1. **Why Doubly Linked List?** We need to delete or move any node in O(1).
2. **Why Hash Map?** We need direct access to a node using its key.
3. **Why store both key and value?** During eviction, we need the key to remove its map entry.
4. **Why dummy HEAD and TAIL?** To avoid special cases during insertion and deletion.
5. **Why insert after HEAD?** HEAD represents the most recently used end.
6. **Why remove `tail.prev`?** It represents the least recently used entry.
7. **Why reuse nodes?** `get()` and updates can move the existing node without unnecessary allocation.
8. **Why delete from the map during eviction?** Otherwise, the map would retain an entry for a node no longer in the cache.

---

## 10. Key Takeaway

```text
LRU Cache
    |
    ├── Hash Map
    |      └── Find node using key
    |
    └── Doubly Linked List
           ├── Maintain recency order
           ├── Insert at front
           ├── Remove any node
           └── Evict from the back
```

**Remember:**

- `head.next` = MRU
- `tail.prev` = LRU
- `get()` = Find + Move to front
- `put()` = Update/Insert + Evict if necessary

The combination of a Hash Map and Doubly Linked List gives us O(1) average time for both `get()` and `put()`.
