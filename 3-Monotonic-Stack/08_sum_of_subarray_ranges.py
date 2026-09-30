"""
Problem:
Find the sum of ranges of all subarrays.

Range of a subarray:
    maximum - minimum

Example:
arr = [1, 4, 3, 2]

Output:
13


Pattern:
Monotonic Stack + Contribution Technique


Key Observation:
Instead of calculating every subarray range:

    range = maximum - minimum

Therefore:

    sum of ranges
    =
    sum of subarray maximums
    -
    sum of subarray minimums


For Minimum:
    PSEE → Previous Smaller OR Equal
    NSE  → Next Strictly Smaller

For Maximum:
    PGE → Previous Greater OR Equal
    NGE  → Next Strictly Greater


Contribution:
For each arr[i]:

    left  = i - previous_boundary
    right = next_boundary - i

    contribution = left × right × arr[i]


Duplicate handling:

Minimum:
    pop >   for PSEE
    pop >=  for NSE

Maximum:
    pop <   for PGE
    pop <=  for NGE


Complexity:
Brute:
    Time  → O(N²)
    Space → O(1)

Optimal:
    Time  → O(N)
    Space → O(N)


Takeaway:
Sum of Subarray Ranges is simply:

    Sum of Subarray Maximums
    -
    Sum of Subarray Minimums

The same contribution technique is used for both.
"""

# --------------------------------------------------
# Brute Force
# --------------------------------------------------

def sum_subarray_ranges_brute(arr):
    n = len(arr)
    total = 0

    for i in range(n):

        largest = arr[i]
        smallest = arr[i]

        for j in range(i + 1, n):

            largest = max(largest, arr[j])
            smallest = min(smallest, arr[j])

            total += largest - smallest

    return total


# --------------------------------------------------
# Sum of Subarray Minimums
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


def sum_subarray_mins(arr):
    psee = find_psee(arr)
    nse = find_nse(arr)

    total = 0

    for i in range(len(arr)):

        left = i - psee[i]
        right = nse[i] - i

        total += left * right * arr[i]

    return total


# --------------------------------------------------
# Sum of Subarray Maximums
# --------------------------------------------------

def find_pge(arr):
    n = len(arr)
    pge = [-1] * n
    stack = []

    for i in range(n):

        while stack and arr[stack[-1]] < arr[i]:
            stack.pop()

        if stack:
            pge[i] = stack[-1]

        stack.append(i)

    return pge


def find_nge(arr):
    n = len(arr)
    nge = [n] * n
    stack = []

    for i in range(n - 1, -1, -1):

        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()

        if stack:
            nge[i] = stack[-1]

        stack.append(i)

    return nge


def sum_subarray_maxs(arr):
    pge = find_pge(arr)
    nge = find_nge(arr)

    total = 0

    for i in range(len(arr)):

        left = i - pge[i]
        right = nge[i] - i

        total += left * right * arr[i]

    return total


# --------------------------------------------------
# Optimal
# --------------------------------------------------

def sum_subarray_ranges(arr):
    return sum_subarray_maxs(arr) - sum_subarray_mins(arr)


# Example
arr = [1, 4, 3, 2]

print("Brute:  ", sum_subarray_ranges_brute(arr))
print("Optimal:", sum_subarray_ranges(arr))
