"""
Problem:
For every element, find the nearest smaller element
on its left.

If no smaller element exists → return -1.

Example:
arr = [4, 5, 2, 10, 8]

Answer:
[-1, 4, -1, 2, 2]


Pattern:
Monotonic Stack → Nearest Smaller Element

Key Observation:
For every element, we only care about the LEFT side.

Therefore:
    Traverse → Left to Right

We need the nearest smaller element.

Maintain an increasing monotonic stack:

    stack.top < current

Before processing current:
    pop all elements >= current

Why?

Those elements cannot be the answer for current
or any future element because current is smaller
and is closer.


Brute:
For every element arr[i], scan towards the left:

    i-1 → i-2 → ... → 0

The first element smaller than arr[i] is the answer.


Optimal:
Traverse from left → right.

Maintain an increasing monotonic stack.

For every element:
    1. Pop elements >= current.
    2. If stack is empty → answer = -1.
    3. Otherwise → stack top is the nearest smaller.
    4. Push current.


Pseudocode:

Brute:
    for i from 0 to N-1:
        for j from i-1 down to 0:
            if arr[j] < arr[i]:
                ans[i] = arr[j]
                break


Optimal:
    create empty stack

    for i from 0 to N-1:

        while stack is not empty
              and stack.top >= arr[i]:
            pop

        if stack is empty:
            ans[i] = -1
        else:
            ans[i] = stack.top

        push arr[i]


Dry Run:
arr = [4, 5, 2, 10, 8]

4:
    stack empty → -1
    push 4

5:
    top = 4 < 5
    answer = 4
    push 5

2:
    5 >= 2 → pop
    4 >= 2 → pop
    stack empty → -1
    push 2

10:
    top = 2 < 10
    answer = 2
    push 10

8:
    10 >= 8 → pop
    top = 2 < 8
    answer = 2
    push 8

Answer:
[-1, 4, -1, 2, 2]


Complexity:

Brute:
Time  → O(N²)
Space → O(N) for answer

Optimal:
Time  → O(N)
Space → O(N)

Although there is a while loop, every element
is pushed once and popped at most once.


Takeaway:
Nearest Smaller on Left:

    Direction → Left → Right
    Stack     → Increasing
    Pop       → >= current
    Answer    → stack.top

Compare with Next Greater:

    NGE:
        Direction → Right → Left
        Stack     → Decreasing
        Pop       → <= current

    NSE:
        Direction → Left → Right
        Stack     → Increasing
        Pop       → >= current
"""


# --------------------------------------------------
# Brute Force
# --------------------------------------------------

def next_smaller_brute(arr):
    n = len(arr)
    ans = [-1] * n

    for i in range(n):

        # Search towards the left
        for j in range(i - 1, -1, -1):

            if arr[j] < arr[i]:
                ans[i] = arr[j]
                break

    return ans


# --------------------------------------------------
# Optimal — Monotonic Stack
# --------------------------------------------------

def next_smaller_optimal(arr):
    n = len(arr)
    ans = [-1] * n
    stack = []

    # Traverse from left → right
    for i in range(n):

        # Remove elements that cannot be smaller
        while stack and stack[-1] >= arr[i]:
            stack.pop()

        # Stack top is the nearest smaller element
        if stack:
            ans[i] = stack[-1]

        # Current element becomes a candidate
        stack.append(arr[i])

    return ans


# Example
arr = [4, 5, 2, 10, 8]

print("Brute:  ", next_smaller_brute(arr))
print("Optimal:", next_smaller_optimal(arr))