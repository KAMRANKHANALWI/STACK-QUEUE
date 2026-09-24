"""
Problem:
Implement a Stack using a Linked List.

Pattern:
Stack → LIFO
Linked List → Dynamic memory

Key Observation:
A Stack only needs insertion and deletion from one end.

So we can use the head of the Linked List as the
top of the Stack.

    top → latest inserted node

Push:
    Add a new node at the head.

Pop:
    Remove the head node.

This gives O(1) for all Stack operations.


Approach:
Use a Linked List with:

    top  → points to the top node
    size → tracks number of elements

Node:
    data
    next


Pseudocode:

push(x):
    new_node = Node(x)
    new_node.next = top
    top = new_node
    size += 1


pop():
    if top is None:
        return None

    temp = top
    top = top.next
    delete temp
    size -= 1


peek():
    if top is None:
        return None

    return top.data


size():
    return size


Dry Run:

push(4):

top → 4 → None

push(2):

top → 2 → 4 → None

push(3):

top → 3 → 2 → 4 → None

push(1):

top → 1 → 3 → 2 → 4 → None

peek() → 1

pop():
remove 1

top → 3 → 2 → 4 → None

peek() → 3


Complexity:
push → O(1)
pop  → O(1)
peek → O(1)
size → O(1)

Space:
O(N)

Takeaway:
For a Stack using Linked List, keep the top at the
head of the list.

Insert at head → push
Delete from head → pop

Unlike an array-based Stack, the Linked List version
does not require a fixed capacity.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, x):
        new_node = Node(x)

        new_node.next = self.top
        self.top = new_node

        self._size += 1

    def pop(self):
        if self.top is None:
            return None

        temp = self.top
        self.top = self.top.next

        self._size -= 1

        return temp.data

    def peek(self):
        if self.top is None:
            return None

        return self.top.data

    def size(self):
        return self._size

    def is_empty(self):
        return self.top is None


# Example
stack = Stack()

stack.push(4)
stack.push(2)
stack.push(3)
stack.push(1)

print(stack.peek())      # 1
print(stack.pop())       # 1
print(stack.peek())      # 3
print(stack.size())      # 3
print(stack.is_empty())  # False