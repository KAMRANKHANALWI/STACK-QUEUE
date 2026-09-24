"""
Problem:
Implement a Queue using an array/list.

Pattern:
Queue → FIFO (First In, First Out)

Key Observation:
Insertion happens at the rear.
Removal happens from the front.

Operations:
- push(x)      → add x to rear
- pop()        → remove front element
- peek()       → return front element
- is_empty()   → check whether queue is empty

Approach:
Use a Python list as the underlying array.

    push → append()
    pop  → remove element from front
    peek → queue[0]

Important:
Using pop(0) is O(N) in Python because all remaining
elements have to be shifted.

For learning the basic array implementation, we use it
to clearly demonstrate the Queue concept.

Production Note:
For a production-quality queue, we'd normally use:

    from collections import deque

with:

    queue.append(x)
    queue.popleft()

giving O(1) insertion/removal from the appropriate ends.

But for this learning problem, keeping the list
implementation is useful because we're explicitly
learning how a queue works using an array.

Dry Run:
push(10) → [10]
push(20) → [10, 20]
push(30) → [10, 20, 30]

peek() → 10
pop()  → 10
queue  → [20, 30]

Complexity:
push     → O(1)
pop      → O(N) with Python list
peek     → O(1)
is_empty → O(1)

Space:
O(N)

Takeaway:
Queue = FIFO.
The first element inserted is the first one removed.
"""


class Queue:
    def __init__(self):
        self.queue = []

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        if self.is_empty():
            return None

        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return None

        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0


# Example
queue = Queue()

queue.push(10)
queue.push(20)
queue.push(30)

print(queue.peek())      # 10
print(queue.pop())       # 10
print(queue.peek())      # 20
print(queue.is_empty())  # False

