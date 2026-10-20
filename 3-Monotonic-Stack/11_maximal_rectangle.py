
"""
Problem:
Given a binary matrix containing only 0s and 1s,
find the maximum area rectangle containing only 1s.

Pattern:
Maximal Rectangle = Histogram + Monotonic Stack

Key Observation:
For each row, calculate consecutive 1s vertically.
These heights form a histogram.

A zero resets the height to zero.

Approach:
1. Maintain histogram heights for every column.
2. Update heights for each row.
3. Find the largest rectangle in that histogram.
4. Track the maximum area across all rows.

Pseudocode:

heights = [0] * columns
max_area = 0

for each row:
    for each column:
        if matrix[row][column] == 1:
            heights[column] += 1
        else:
            heights[column] = 0

    area = largest_rectangle_in_histogram(heights)
    max_area = max(max_area, area)

return max_area

Complexity:
Let N = number of rows, M = number of columns.

Time  -> O(N * M)
Space -> O(M), excluding the input matrix

Takeaway:
Every row becomes a histogram.
Reuse the Largest Rectangle in Histogram solution.
"""


def largest_rectangle_in_histogram(heights):
    stack = []
    max_area = 0
    n = len(heights)

    # The extra iteration processes remaining bars.
    for i in range(n + 1):
        while stack and (
            i == n or heights[stack[-1]] > heights[i]
        ):
            index = stack.pop()

            height = heights[index]
            pse = stack[-1] if stack else -1
            nse = i

            width = nse - pse - 1
            area = height * width

            max_area = max(max_area, area)

        if i < n:
            stack.append(i)

    return max_area


def maximal_rectangle(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])

    heights = [0] * cols
    max_area = 0

    for i in range(rows):
        for j in range(cols):

            # Extend the histogram or reset at zero.
            if matrix[i][j] == "1" or matrix[i][j] == 1:
                heights[j] += 1
            else:
                heights[j] = 0

        # Solve the current row as a histogram.
        area = largest_rectangle_in_histogram(heights)
        max_area = max(max_area, area)

    return max_area


# Example
matrix = [
    ["1", "0", "1", "0", "1"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]

print(maximal_rectangle(matrix))  # 6
