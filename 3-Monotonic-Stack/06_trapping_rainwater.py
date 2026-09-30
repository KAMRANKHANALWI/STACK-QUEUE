"""
Problem:
Given an array of bar heights, calculate how much
rainwater can be trapped between the bars.

Example:
arr = [0,1,0,2,1,0,1,3,2,1,2,1]

Output:
6


Pattern:
Trapping Rainwater → Prefix/Suffix Maximums
                    → Two Pointers


Key Observation:
For every index i, water can be trapped only if there
is a taller/equal bar on BOTH sides.

The water level at i is:

    min(leftMax, rightMax)

Therefore:

    water[i] = min(leftMax, rightMax) - arr[i]


Brute:
For every index:

    1. Find maximum height on the left.
    2. Find maximum height on the right.
    3. Add:

       min(leftMax, rightMax) - arr[i]


Brute Complexity:
Time  → O(N²)
Space → O(1)


Better — Prefix/Suffix Maximum:
Precompute:

    prefix[i] = maximum height from 0 → i
    suffix[i] = maximum height from i → N-1

Then:

    water[i] = min(prefix[i], suffix[i]) - arr[i]


Pseudocode:

    prefix[0] = arr[0]

    for i from 1 to N-1:
        prefix[i] = max(prefix[i-1], arr[i])


    suffix[N-1] = arr[N-1]

    for i from N-2 down to 0:
        suffix[i] = max(suffix[i+1], arr[i])


    total = 0

    for i from 0 to N-1:
        water = min(prefix[i], suffix[i]) - arr[i]
        total += water


Better Complexity:
Time  → O(N)
Space → O(N)


Optimal — Two Pointers:
We don't actually need the complete prefix/suffix arrays.

Maintain:

    leftMax  → maximum height seen from left
    rightMax → maximum height seen from right

Use two pointers:

    l = 0
    r = N - 1

If:

    arr[l] <= arr[r]

then the left side is the limiting side.

So we can safely calculate water at l.

Otherwise:

    right side is limiting
    calculate water at r.


Pseudocode:

    left = 0
    right = N - 1

    leftMax = 0
    rightMax = 0
    total = 0

    while left < right:

        if arr[left] <= arr[right]:

            if arr[left] >= leftMax:
                leftMax = arr[left]
            else:
                total += leftMax - arr[left]

            left += 1

        else:

            if arr[right] >= rightMax:
                rightMax = arr[right]
            else:
                total += rightMax - arr[right]

            right -= 1


Why does this work?

If:

    arr[left] <= arr[right]

then there is a right boundary at least as high as
arr[left].

Therefore the amount of water at left depends only on
leftMax:

    water = leftMax - arr[left]

Similarly, when:

    arr[right] < arr[left]

the right side is the limiting side:

    water = rightMax - arr[right]


Dry Run:

arr = [0,1,0,2,1,0,1,3,2,1,2,1]

The trapped water at each index is:

    [0,0,1,0,1,2,1,0,0,1,0,0]

Total:

    0 + 0 + 1 + 0 + 1 + 2 + 1 + 0 + 0 + 1
    = 6


Complexity:

Brute:
Time  → O(N²)
Space → O(1)

Prefix/Suffix:
Time  → O(N)
Space → O(N)

Optimal — Two Pointers:
Time  → O(N)
Space → O(1)


Takeaway:

Trapping Rainwater:

    water[i]
        =
    min(leftMax, rightMax) - arr[i]

Optimization:

    Prefix/Suffix arrays
          ↓
    Two pointers

Two-pointer idea:

    arr[left] <= arr[right]
        → process LEFT

    arr[left] > arr[right]
        → process RIGHT
"""


# --------------------------------------------------
# Brute Force
# --------------------------------------------------

def trap_brute(arr):
    n = len(arr)
    total = 0

    for i in range(n):

        left_max = 0
        right_max = 0

        # Maximum height on the left
        for j in range(i + 1):
            left_max = max(left_max, arr[j])

        # Maximum height on the right
        for j in range(i, n):
            right_max = max(right_max, arr[j])

        # Water trapped at current index
        total += min(left_max, right_max) - arr[i]

    return total


# --------------------------------------------------
# Better — Prefix/Suffix Maximum
# --------------------------------------------------

def trap_prefix_suffix(arr):
    n = len(arr)

    if n == 0:
        return 0

    prefix = [0] * n
    suffix = [0] * n

    # Maximum height from left
    prefix[0] = arr[0]

    for i in range(1, n):
        prefix[i] = max(prefix[i - 1], arr[i])

    # Maximum height from right
    suffix[n - 1] = arr[n - 1]

    for i in range(n - 2, -1, -1):
        suffix[i] = max(suffix[i + 1], arr[i])

    total = 0

    for i in range(n):
        total += min(prefix[i], suffix[i]) - arr[i]

    return total


# --------------------------------------------------
# Optimal — Two Pointers
# --------------------------------------------------

def trap_optimal(arr):
    n = len(arr)

    if n == 0:
        return 0

    left = 0
    right = n - 1

    left_max = 0
    right_max = 0

    total = 0

    while left < right:

        if arr[left] <= arr[right]:

            if arr[left] >= left_max:
                left_max = arr[left]
            else:
                total += left_max - arr[left]

            left += 1

        else:

            if arr[right] >= right_max:
                right_max = arr[right]
            else:
                total += right_max - arr[right]

            right -= 1

    return total


# --------------------------------------------------
# Example
# --------------------------------------------------

arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print("Brute:         ", trap_brute(arr))
print("Prefix/Suffix: ", trap_prefix_suffix(arr))
print("Optimal:       ", trap_optimal(arr))