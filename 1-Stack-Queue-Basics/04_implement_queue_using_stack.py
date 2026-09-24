"""
Problem:
Implement a Queue using Stack(s).

Pattern:
Queue → FIFO
Stack → LIFO

Key Observation:
A Stack removes the newest element first, but a Queue
needs to remove the oldest element first.

So we need to reverse the order of elements using
one or two stacks.


Approach 1: Using Two Stacks - Costly Push
-------------------------------------------
Use input and output stacks.

For push(x):
1. Move all elements from input → output.
2. Push x into input.
3. Move all elements from output → input.

This keeps the oldest element at the top of input.

pop():
    Remove from input.

top():
    Return the top of input.


Pseudocode:

push(x):
    while input is not empty:
        output.push(input.pop())

    input.push(x)

    while output is not empty:
        input.push(output.pop())

pop():
    input.pop()

top():
    return input.top()


Complexity:
push → O(N)
pop  → O(1)
top  → O(1)
Space → O(N)


Example:

Before push(3):
input = [2, 5]

push(3):

Move input → output:
output = [5, 2]

Push 3:
input = [3]

Move output → input:
input = [2, 5, 3]

Now the oldest element 2 is at the top.

So:

pop() → 2
top() → 5


Approach 2: Using Two Stacks - Costly Pop (Optimized)
-------------------------------------------------------
Use two stacks:

    input  → receives new elements
    output → provides elements for pop/top

For push(x):
    Add x to input.

For pop():
1. If output is not empty, pop from output.
2. If output is empty, transfer all elements
   from input → output.
3. Pop from output.

For top():
1. If output is not empty, return output.top().
2. Otherwise transfer input → output.
3. Return output.top().


Pseudocode:

push(x):
    input.push(x)


pop():
    if output is not empty:
        return output.pop()

    while input is not empty:
        output.push(input.pop())

    return output.pop()


top():
    if output is not empty:
        return output.top()

    while input is not empty:
        output.push(input.pop())

    return output.top()


Complexity:
push → O(1)

pop:
- Worst case → O(N)
- Amortized → O(1)

top:
- Worst case → O(N)
- Amortized → O(1)

Space → O(N)


Dry Run:

push(2):
input = [2]

push(5):
input = [2, 5]

push(3):
input = [2, 5, 3]

top():

output is empty
→ move input → output

input  = []
output = [3, 5, 2]

top() → 2


pop() → 2

output = [3, 5]

push(6):

input  = [6]
output = [3, 5]

pop() → 5

output = [3]

pop() → 3

output = []

pop():

output is empty
→ move input → output

input  = []
output = [6]

pop() → 6


Takeaway:
To implement FIFO using LIFO, we need to reverse the
order of elements.

Two stacks give us two approaches:

Costly Push:
    push  → O(N)
    pop   → O(1)

Costly Pop:
    push  → O(1)
    pop   → O(1) amortized

The costly-pop approach is preferred because elements
are transferred only when the output stack is empty.
"""


class Queue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        # New elements always enter the input stack
        self.input.append(x)

    def _transfer(self):
        # Transfer only when output is empty
        while self.input:
            self.output.append(self.input.pop())

    def pop(self):
        if not self.output:
            self._transfer()

        if not self.output:
            return None

        return self.output.pop()

    def top(self):
        if not self.output:
            self._transfer()

        if not self.output:
            return None

        return self.output[-1]

    def is_empty(self):
        return not self.input and not self.output


# Example
queue = Queue()

queue.push(2)
queue.push(5)
queue.push(3)

print(queue.top())       # 2
print(queue.pop())       # 2

queue.push(6)

print(queue.pop())       # 5
print(queue.pop())       # 3
print(queue.pop())       # 6

print(queue.is_empty())  # True