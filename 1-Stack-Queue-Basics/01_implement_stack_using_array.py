"""
Problem:
Implement a Stack using an array/list.

Pattern:
Stack → LIFO (Last In, First Out)

Key Observation:
All stack operations happen at one end → the top.

Operations:
- push(x) → add x to top
- pop()   → remove top element
- peek()  → return top element
- is_empty() → check whether stack is empty

Approach:
Use a Python list as the underlying array.

    push → append()
    pop  → pop()
    peek → stack[-1]

Dry Run:
push(10) → [10]
push(20) → [10, 20]
push(30) → [10, 20, 30]

peek() → 30
pop()  → 30
stack  → [10, 20]

Complexity:
push     → O(1)
pop      → O(1)
peek     → O(1)
is_empty → O(1)

Space:
O(N)

Takeaway:
Stack = LIFO.
The last element inserted is the first one removed.
"""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.is_empty():
            return None

        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None

        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0


# Example
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print(stack.peek())      # 30
print(stack.pop())       # 30
print(stack.peek())      # 20
print(stack.is_empty())  # False
