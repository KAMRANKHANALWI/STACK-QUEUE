"""
Problem:
Given a circular array, find the Next Greater Element
for every element.

If no greater element exists → return -1.

Example:
arr = [2, 10, 12, 1, 11]

Answer:
[10, 12, -1, 11, 12]


Pattern:
Monotonic Stack → Next Greater Element II

Key Observation:
Same NGE idea, but after the last element we continue
from the beginning.

We can simulate the circular array by imagining 2N
positions and mapping every index using:

    index % N


Hypothetical:

    [2, 10, 12, 1, 11, 2, 10, 12, 1, 11]
     └──── original ────┘ └── circular ──┘

We don't actually create this array.


Brute:
For every element, check the next N-1 elements
using:

    (i + j) % N


Optimal:
Traverse the hypothetical 2N array from right → left.

For every index:

    current = arr[i % N]

Maintain a decreasing monotonic stack.

1. Pop elements <= current.
2. Stack top is the next greater element.
3. Push current.

Only fill answers when i < N because those are the
original array indices.


Pseudocode:

Brute:
    for i from 0 to N-1:
        for j from 1 to N-1:
            index = (i + j) % N

            if arr[index] > arr[i]:
                ans[i] = arr[index]
                break


Optimal:
    for i from 2N-1 down to 0:
        current = arr[i % N]

        while stack is not empty
              and stack.top <= current:
            pop

        if i < N:
            if stack is not empty:
                ans[i] = stack.top

        push current


Dry Run:
arr = [2, 10, 12, 1, 11]

11 → 2 → 10 → 12
              → NGE = 12

1 → 11
  → NGE = 11

12 → no greater element
   → NGE = -1

Answer:
[10, 12, -1, 11, 12]


Complexity:

Brute:
Time  → O(N²)
Space → O(1) auxiliary

Optimal:
Time  → O(N)
Space → O(N)


Takeaway:
NGE-II = NGE-I + Circular Array.

Circular array:
    index → index % N

NGE:
    traverse right → left
    maintain decreasing stack
    pop elements <= current
    stack top = next greater element
"""


# --------------------------------------------------
# Brute Force
# --------------------------------------------------

def next_greater_brute(arr):
    n = len(arr)
    ans = [-1] * n

    for i in range(n):

        for j in range(1, n):
            index = (i + j) % n

            if arr[index] > arr[i]:
                ans[i] = arr[index]
                break

    return ans


# --------------------------------------------------
# Optimal — Monotonic Stack
# --------------------------------------------------

def next_greater_optimal(arr):
    n = len(arr)
    ans = [-1] * n
    stack = []

    # Simulate a circular array using 2N positions
    for i in range(2 * n - 1, -1, -1):

        current = arr[i % n]

        # Remove elements that cannot be NGE
        while stack and stack[-1] <= current:
            stack.pop()

        # Only original indices need answers
        if i < n and stack:
            ans[i] = stack[-1]

        stack.append(current)

    return ans


# Example
arr = [2, 10, 12, 1, 11]

print("Brute:  ", next_greater_brute(arr))
print("Optimal:", next_greater_optimal(arr))