
"""
Problem:
Design an LRU (Least Recently Used) Cache.

Operations:
- get(key)        -> return value, or -1 if absent
- put(key, value) -> insert or update a key-value pair

Pattern:
Hash Map + Doubly Linked List

Key Observation:
1. Hash Map → find a node using its key in O(1) average.
2. Doubly Linked List → insert/delete any node in O(1).

Linked List Order:
HEAD -> MRU -> ... -> LRU -> TAIL

Rules:
- head.next = Most Recently Used node
- tail.prev = Least Recently Used node
- New/recently accessed nodes go after HEAD.
- When full, evict tail.prev.

Complexity:
get()  -> O(1) average
put()  -> O(1) average
Space  -> O(capacity)

Takeaway:
Hash Map finds the node.
Doubly Linked List maintains recency order.
"""


# --------------------------------------------------
# Doubly Linked List Node
# --------------------------------------------------

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

        self.prev = None
        self.next = None


# --------------------------------------------------
# LRU Cache
# --------------------------------------------------

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        # Key -> Node reference
        self.cache = {}

        # Dummy head and tail
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        # Initially, head and tail are connected
        self.head.next = self.tail
        self.tail.prev = self.head

    # ----------------------------------------------
    # Remove a node from its current position
    # ----------------------------------------------

    def remove(self, node):

        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    # ----------------------------------------------
    # Insert a node immediately after HEAD
    # ----------------------------------------------

    def insert_after_head(self, node):

        curr_after_head = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = curr_after_head
        curr_after_head.prev = node

    # ----------------------------------------------
    # GET
    # ----------------------------------------------

    def get(self, key: int) -> int:

        # Key doesn't exist
        if key not in self.cache:
            return -1

        node = self.cache[key]
        value = node.value

        # Mark as recently used
        self.remove(node)
        self.insert_after_head(node)

        return value

    # ----------------------------------------------
    # PUT
    # ----------------------------------------------

    def put(self, key: int, value: int) -> None:

        # Case 1: Key already exists
        if key in self.cache:

            node = self.cache[key]

            # Update existing value
            node.value = value

            # Mark as recently used
            self.remove(node)
            self.insert_after_head(node)

        # Case 2: New key
        else:

            # Evict LRU node if cache is full
            if len(self.cache) == self.capacity:

                lru_node = self.tail.prev

                # Remove from Hash Map
                del self.cache[lru_node.key]

                # Remove from Doubly Linked List
                self.remove(lru_node)

            # Create new node
            new_node = Node(key, value)

            # Add to Hash Map
            self.cache[key] = new_node

            # Add to front of Linked List
            self.insert_after_head(new_node)


# --------------------------------------------------
# Example
# --------------------------------------------------

lru = LRUCache(2)

lru.put(1, 1)
lru.put(2, 2)

print(lru.get(1))  # 1

lru.put(3, 3)      # Evicts key 2

print(lru.get(2))  # -1

lru.put(4, 4)      # Evicts key 1

print(lru.get(1))  # -1
print(lru.get(3))  # 3
print(lru.get(4))  # 4
