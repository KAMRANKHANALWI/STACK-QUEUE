"""
Problem:
For every element, find the first greater element to its right.

If no greater element exists → return -1.

Example:
arr = [6, 0, 8, 1, 3]

Answer:
[8, 8, -1, 3, -1]


Pattern:
Monotonic Stack → Next Greater Element

Key Observation:
For arr[i], we only care about the first element to the
right that is strictly greater than arr[i].

Brute:
For every element, scan all elements to its right.

Optimal:
Traverse from right → left and maintain a decreasing
monotonic stack.

Why does the stack work?

For current element x:

1. Remove all elements <= x.
   They can never be the answer for x.

2. Stack top is now the nearest greater element.

3. Push x for elements on its left.


Pseudocode:

Brute:
    for i from 0 to n-1:
        for j from i+1 to n-1:
            if arr[j] > arr[i]:
                ans[i] = arr[j]
                break


Optimal:
    for i from n-1 to 0:
        while stack is not empty and stack.top <= arr[i]:
            pop

        if stack is empty:
            ans[i] = -1
        else:
            ans[i] = stack.top

        push arr[i]


Dry Run:
arr = [6, 0, 8, 1, 3]

3 → -1 → stack = [3]
1 → 3  → stack = [3, 1]
8 → -1 → stack = [8]
0 → 8  → stack = [8, 0]
6 → 8  → stack = [8, 6]

Answer:
[8, 8, -1, 3, -1]


Complexity:

Brute:
Time  → O(N²)
Space → O(1) auxiliary

Optimal:
Time  → O(N)
Space → O(N)


Takeaway:
Next Greater Element → think Monotonic Stack.

For NGE:
- Traverse right → left
- Maintain decreasing stack
- Pop elements <= current
- Stack top = next greater element
"""


# --------------------------------------------------
# Brute Force
# --------------------------------------------------

def next_greater_brute(arr):
    n = len(arr)
    ans = [-1] * n

    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                ans[i] = arr[j]
                break

    return ans


# --------------------------------------------------
# Optimal — Monotonic Stack
# --------------------------------------------------

def next_greater_optimal(arr):
    n = len(arr)
    ans = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):

        while stack and stack[-1] <= arr[i]:
            stack.pop()

        if stack:
            ans[i] = stack[-1]

        stack.append(arr[i])

    return ans


# Example
arr = [6, 0, 8, 1, 3]

print("Brute:  ", next_greater_brute(arr))
print("Optimal:", next_greater_optimal(arr))