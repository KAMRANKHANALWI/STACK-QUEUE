"""
Problem:
Given the heights of histogram bars, find the area of the
largest rectangle that can be formed.

Example:
heights = [2, 1, 5, 6, 2, 3]

Output:
10

Pattern:
Monotonic Increasing Stack

Key Observation:
For every bar, treat its height as the rectangle's minimum
height and find how far it can extend in both directions.

PSE = Previous Smaller Element's index
NSE = Next Smaller Element's index

    width = NSE - PSE - 1
    area  = height[i] * width

If no smaller element exists:
    PSE = -1
    NSE = n


Brute Force:
For every bar:
    1. Expand left while bars are >= current height.
    2. Expand right while bars are >= current height.
    3. Calculate the rectangle area.

Pseudocode — Brute:

    max_area = 0

    for i from 0 to n - 1:
        left = i
        right = i

        while left > 0 and heights[left - 1] >= heights[i]:
            left -= 1

        while right < n - 1 and heights[right + 1] >= heights[i]:
            right += 1

        width = right - left + 1
        max_area = max(max_area, heights[i] * width)

    return max_area


Optimal Approach:
Use an increasing stack of indices.

Traverse from left to right:
    While current height < height at stack top:
        Pop the top index.
        The current index is its NSE.
        The new stack top is its PSE.
        Calculate the area.

After traversal:
    Pop remaining indices.
    Their NSE is n.

Pseudocode — Optimal:

    stack = []
    max_area = 0

    for i from 0 to n:
        while stack and (i == n or heights[stack[-1]] > heights[i]):
            index = stack.pop()

            nse = i
            pse = stack[-1] if stack else -1

            width = nse - pse - 1
            area = heights[index] * width

            max_area = max(max_area, area)

        if i < n:
            stack.append(i)

    return max_area


Dry Run:
heights = [2, 1, 5, 6, 2, 3]

Bar 5 at index 2:
    PSE = index 1, height 1
    NSE = index 4, height 2
    width = 4 - 1 - 1 = 2
    area = 5 * 2 = 10

Bar 6 at index 3:
    PSE = index 2, height 5
    NSE = index 4, height 2
    width = 4 - 2 - 1 = 1
    area = 6 * 1 = 6

Maximum area = 10


Complexity:
Brute:
    Time  -> O(N^2)
    Space -> O(1)

Optimal:
    Time  -> O(N)
    Space -> O(N)

Takeaway:
When a smaller bar appears, taller bars can no longer
extend beyond that boundary.

Pop the bar, find its width using PSE and NSE,
and calculate its maximum possible rectangle area.
"""


# --------------------------------------------------
# Brute Force
# --------------------------------------------------

def largest_rectangle_brute(heights):
    n = len(heights)
    max_area = 0

    for i in range(n):
        left = i
        right = i

        # Expand left while bars can support this height.
        while left > 0 and heights[left - 1] >= heights[i]:
            left -= 1

        # Expand right while bars can support this height.
        while right < n - 1 and heights[right + 1] >= heights[i]:
            right += 1

        width = right - left + 1
        area = heights[i] * width

        max_area = max(max_area, area)

    return max_area


# --------------------------------------------------
# Optimal — Monotonic Stack
# --------------------------------------------------

def largest_rectangle_optimal(heights):
    n = len(heights)
    stack = []
    max_area = 0

    # i == n flushes bars that have no smaller bar on the right.
    for i in range(n + 1):

        while stack and (
            i == n or heights[stack[-1]] > heights[i]
        ):
            index = stack.pop()

            # Current index is the next smaller boundary.
            nse = i

            # New stack top is the previous smaller boundary.
            pse = stack[-1] if stack else -1

            width = nse - pse - 1
            area = heights[index] * width

            max_area = max(max_area, area)

        if i < n:
            stack.append(i)

    return max_area


# Example
heights = [2, 1, 5, 6, 2, 3]

print("Brute:  ", largest_rectangle_brute(heights))
print("Optimal:", largest_rectangle_optimal(heights))

# Brute:   10
# Optimal: 10
