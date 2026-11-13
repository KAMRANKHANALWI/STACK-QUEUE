"""
Problem:
Design an LFU (Least Frequently Used) Cache.

Operations:
- get(key)        -> return value, or -1 if absent
- put(key, value) -> insert or update a key-value pair

Eviction Rules:
1. Remove the least frequently used key.
2. If frequencies tie, remove the least recently used key.

Pattern:
Hash Maps + Doubly Linked Lists

Data Structures:
- key_to_node  -> key to Node
- freq_to_dll  -> frequency to DLL
- min_freq     -> minimum frequency in cache

Complexity:
get()  -> O(1) average
put()  -> O(1) average
Space  -> O(capacity)

Takeaway:
Multiple LRU lists grouped by frequency.
"""


# --------------------------------------------------
# Node
# --------------------------------------------------
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1

        self.prev = None
        self.next = None


# --------------------------------------------------
# Doubly Linked List
# --------------------------------------------------
class DLL:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    # Insert node immediately after HEAD
    def insert_front(self, node):

        curr_after_head = self.head.next

        node.next = curr_after_head
        node.prev = self.head

        curr_after_head.prev = node
        self.head.next = node

        self.size += 1

    # Remove a given node
    def remove(self, node):

        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

        self.size -= 1

    # Remove the LRU node
    def remove_lru(self):
        if self.size == 0:
            return None

        node = self.tail.prev
        self.remove(node)

        return node


# --------------------------------------------------
# LFU Cache
# --------------------------------------------------


class LFUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0

        # Key -> Node
        self.key_to_node = {}

        # Frequency -> Doubly Linked List
        self.freq_to_dll = {}

        # Minimum frequency currently present
        self.min_freq = 0

    # ----------------------------------------------
    # Increase frequency and move node
    # ----------------------------------------------

    def update_freq(self, node):

        freq = node.freq

        # Get current frequency list
        dll = self.freq_to_dll[freq]

        # Remove node from current frequency
        dll.remove(node)

        # Update minimum frequency if necessary
        if dll.size == 0 and self.min_freq == freq:
            self.min_freq += 1

        # Increase frequency
        node.freq += 1

        new_freq = node.freq

        # Create new frequency list if needed
        if new_freq not in self.freq_to_dll:
            self.freq_to_dll[new_freq] = DLL()

        # Insert at front (most recently used)
        self.freq_to_dll[new_freq].insert_front(node)

    # ----------------------------------------------
    # GET
    # ----------------------------------------------

    def get(self, key):
        # Key does not exist
        if key not in self.key_to_node:
            return -1

        node = self.key_to_node[key]

        # Successful access increases frequency
        self.update_freq(node)

        return node.value

    # ----------------------------------------------
    # PUT
    # ----------------------------------------------

    def put(self, key, value):

        # Handle zero capacity
        if self.capacity == 0:
            return

        # Case 1: Key already exists
        if key in self.key_to_node:

            node = self.key_to_node[key]

            # Update value
            node.value = value

            # Updating also increases frequency
            self.update_freq(node)

            return

        # Case 2: Cache is full
        if self.size == self.capacity:

            # Get minimum frequency DLL
            dll = self.freq_to_dll[self.min_freq]

            # Remove LRU node
            lfu_node = dll.remove_lru()

            # Remove evicted key from Hash Map
            del self.key_to_node[lfu_node.key]

            self.size -= 1

        # Case 3: Insert new node
        node = Node(key, value)

        # New node always starts at frequency 1
        self.min_freq = 1

        # Create frequency 1 DLL if needed
        if 1 not in self.freq_to_dll:
            self.freq_to_dll[1] = DLL()

        # Insert at front
        self.freq_to_dll[1].insert_front(node)

        # Update key mapping
        self.key_to_node[key] = node

        self.size += 1


# --------------------------------------------------
# Example
# --------------------------------------------------

lfu = LFUCache(2)

lfu.put(1, 1)
lfu.put(2, 2)

print(lfu.get(1))  # 1

lfu.put(3, 3)  # Evicts key 2

print(lfu.get(2))  # -1
print(lfu.get(3))  # 3

lfu.put(4, 4)  # Evicts key 1

print(lfu.get(1))  # -1
print(lfu.get(3))  # 3
print(lfu.get(4))  # 4
