"""
Problem:
Implement a Stack using Queue(s).

Pattern:
Stack → LIFO
Queue → FIFO

Key Observation:
A Queue removes the oldest element first, but a Stack
needs to remove the newest element first.

So we must rearrange the Queue after every push so that
the newest element comes to the front.

Approach 1: Using Two Queues
--------------------------------
Use q1 and q2.

push(x):
1. Add x to q2.
2. Move all elements from q1 to q2.
3. Swap q1 and q2.

Now the newest element is always at the front of q1.

pop():
    Remove from the front of q1.

top():
    Return the front of q1.


Pseudocode:

push(x):
    q2.push(x)

    while q1 is not empty:
        q2.push(q1.front())
        q1.pop()

    swap(q1, q2)

pop():
    q1.pop()

top():
    return q1.front()


Complexity:
push → O(N)
pop  → O(1)
top  → O(1)
Space → O(N)


Approach 2: Using One Queue (Optimized)
----------------------------------------
We can avoid the second queue.

push(x):
1. Add x to the queue.
2. Move the previous elements behind x.

If the queue has N elements after inserting x,
rotate the first N - 1 elements:

    queue.push(queue.front())
    queue.pop()

This places x at the front.

Example:

Before push(30):
queue = [10, 20]

Add 30:
queue = [10, 20, 30]

Rotate N - 1 = 2 elements:
queue = [30, 10, 20]

Now the newest element is at the front.

Pseudocode:

push(x):
    q.push(x)

    for i = 0 to size - 2:
        q.push(q.front())
        q.pop()

pop():
    q.pop()

top():
    return q.front()


Complexity:
push → O(N)
pop  → O(1)
top  → O(1)
Space → O(N)

Dry Run:

push(3):
queue = [3]

push(4):
queue = [3, 4]
rotate 3
queue = [4, 3]

push(2):
queue = [4, 3, 2]
rotate 4, 3
queue = [2, 4, 3]

push(1):
queue = [2, 4, 3, 1]
rotate 2, 4, 3
queue = [1, 2, 4, 3]

top() → 1
pop() → 1
top() → 2

Takeaway:
To implement LIFO using FIFO, keep the newest element
at the front of the Queue.

Two queues → easier to understand.
One queue → optimized space and simpler implementation.
"""


class Stack:
    def __init__(self):
        self.queue = []

    def push(self, x):
        # Add the new element
        self.queue.append(x)

        # Move previous elements behind the new element
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))

    def pop(self):
        if self.is_empty():
            return None

        return self.queue.pop(0)

    def top(self):
        if self.is_empty():
            return None

        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0


# Example
stack = Stack()

stack.push(3)
stack.push(4)
stack.push(2)
stack.push(1)

print(stack.top())       # 1
print(stack.pop())       # 1
print(stack.top())       # 2
print(stack.pop())       # 2
print(stack.is_empty())  # False