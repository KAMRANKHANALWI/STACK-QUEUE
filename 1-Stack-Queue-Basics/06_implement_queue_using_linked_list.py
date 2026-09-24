"""
Problem:
Implement a Queue using a Linked List.

Pattern:
Queue → FIFO
Linked List → Dynamic memory

Key Observation:
A Queue needs insertion at the rear and removal from
the front.

So maintain two pointers:

    front → first element
    rear  → last element

Push:
    Insert at rear.

Pop:
    Remove from front.

This gives O(1) for both operations.


Approach:
Use a Linked List with:

    front → first node
    rear  → last node
    size  → number of elements

Empty Queue:

front = None
rear  = None


Push(x):

If Queue is empty:
    front = rear = new_node

Otherwise:
    rear.next = new_node
    rear = new_node

Then:
    size += 1


Pop():

If Queue is empty:
    return None

Store front temporarily.

Move:
    front = front.next

Delete temporary node.

If front becomes None:
    rear = None

Then:
    size -= 1


Pseudocode:

push(x):
    new_node = Node(x)

    if front is None:
        front = rear = new_node
    else:
        rear.next = new_node
        rear = new_node

    size += 1


pop():
    if front is None:
        return None

    temp = front
    front = front.next

    if front is None:
        rear = None

    size -= 1

    return temp.data


peek():
    if front is None:
        return None

    return front.data


Dry Run:

push(7):

front → 7 ← rear

push(2):

front → 7 → 2 ← rear

push(3):

front → 7 → 2 → 3 ← rear

push(5):

front → 7 → 2 → 3 → 5 ← rear

peek() → 7

pop():
remove 7

front → 2 → 3 → 5 ← rear

pop():
remove 2

front → 3 → 5 ← rear

pop():
remove 3

front → 5 ← rear

peek() → 5

pop():
remove 5

front = None
rear  = None


Complexity:
push → O(1)
pop  → O(1)
peek → O(1)
size → O(1)

Space:
O(N)

Takeaway:
For a Queue using Linked List:

    front → removal
    rear  → insertion

Insert at rear → push/enqueue
Remove from front → pop/dequeue

Unlike an array-based Queue, the Linked List version
does not require a fixed capacity.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def push(self, x):
        new_node = Node(x)

        # First element
        if self.front is None:
            self.front = self.rear = new_node

        # Add at rear
        else:
            self.rear.next = new_node
            self.rear = new_node

        self._size += 1

    def pop(self):
        if self.front is None:
            return None

        temp = self.front
        self.front = self.front.next

        # Queue became empty
        if self.front is None:
            self.rear = None

        self._size -= 1

        return temp.data

    def peek(self):
        if self.front is None:
            return None

        return self.front.data

    def size(self):
        return self._size

    def is_empty(self):
        return self.front is None


# Example
queue = Queue()

queue.push(7)
queue.push(2)
queue.push(3)
queue.push(5)

print(queue.peek())       # 7
print(queue.pop())        # 7
print(queue.pop())        # 2
print(queue.peek())       # 3
print(queue.size())       # 2
print(queue.is_empty())   # False