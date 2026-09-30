"""
Problem:
Find the sum of the minimum element of every subarray.

Example:
arr = [3, 1, 2, 4]
Output = 17


Pattern:
Monotonic Stack + Contribution Technique


Key Observation:
For each arr[i], count how many subarrays have arr[i]
as their minimum.

    contribution = left × right × arr[i]

where:

    left  = i - PSEE[i]
    right = NSE[i] - i

PSEE = Previous Smaller OR Equal
NSE  = Next Strictly Smaller

Why left × right?

    PSEE ← arr[i] → NSE
      ↓                ↓
    choices          choices
     left             right

Every valid start can pair with every valid end.

    count = left × right

So:

    contribution = left × right × arr[i]


Duplicates:
Use asymmetric comparisons:

PSEE → pop while arr[stack[-1]] > arr[i]
NSE  → pop while arr[stack[-1]] >= arr[i]

This assigns equal elements consistently.


Example:
arr = [1, 4, 6, 7, 3, 7, 8, 1]

For 3 at index 4:

    PSEE = 0
    NSE  = 7

    left  = 4
    right = 3

    count = 4 × 3 = 12
    contribution = 12 × 3 = 36


Complexity:
Brute   → O(N²) time, O(1) extra space
Optimal → O(N) time, O(N) space


Takeaway:
Don't find the minimum of every subarray.

Find how many subarrays each element contributes to.

    PSEE → left choices
    NSE  → right choices

    contribution = left × right × arr[i]
"""

MOD = 10**9 + 7


# --------------------------------------------------
# Brute Force
# --------------------------------------------------

def sum_subarray_mins_brute(arr):
    total = 0

    for i in range(len(arr)):
        current_min = float("inf")

        for j in range(i, len(arr)):
            current_min = min(current_min, arr[j])
            total = (total + current_min) % MOD

    return total


# --------------------------------------------------
# PSEE — Previous Smaller OR Equal
# --------------------------------------------------

def find_psee(arr):
    n = len(arr)
    psee = [-1] * n
    stack = []

    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()

        if stack:
            psee[i] = stack[-1]

        stack.append(i)

    return psee


# --------------------------------------------------
# NSE — Next Strictly Smaller
# --------------------------------------------------

def find_nse(arr):
    n = len(arr)
    nse = [n] * n
    stack = []

    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()

        if stack:
            nse[i] = stack[-1]

        stack.append(i)

    return nse


# --------------------------------------------------
# Optimal — Contribution Technique
# --------------------------------------------------

def sum_subarray_mins_optimal(arr):
    psee = find_psee(arr)
    nse = find_nse(arr)

    total = 0

    for i in range(len(arr)):
        left = i - psee[i]
        right = nse[i] - i

        total = (total + left * right * arr[i]) % MOD

    return total


# Example
arr = [3, 1, 2, 4]

print("Brute:   ", sum_subarray_mins_brute(arr))
print("Optimal: ", sum_subarray_mins_optimal(arr))