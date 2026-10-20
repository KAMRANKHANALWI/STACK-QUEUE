# 11. Maximal Rectangle

## Problem

Given a binary matrix containing only `0`s and `1`s, find the maximum
area of a rectangle containing only `1`s.

Example:

``` text
matrix =
1 0 1 0 1
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 6
```

## Pattern

**Binary Matrix → Histogram → Largest Rectangle in Histogram**

This problem reuses the solution from **10. Largest Rectangle in
Histogram**.

## Key Observation

For every column, maintain the number of consecutive `1`s ending at the
current row.

-   If the current cell is `1`, increase that column's height.
-   If the current cell is `0`, reset that column's height to `0`.
-   After processing a row, treat `heights` as a histogram and find its
    largest rectangle.

These are **vertical consecutive heights**, not horizontal prefix sums.

## Visual Intuition

Original matrix:

``` text
        columns
        0 1 2 3 4
      +-----------
row 0 | 1 0 1 0 1
row 1 | 1 0 1 1 1
row 2 | 1 1 1 1 1
row 3 | 1 0 0 1 0
```

After processing row `0`:

``` text
Matrix row:  1 0 1 0 1
Heights:     1 0 1 0 1
```

After processing row `1`:

``` text
Matrix row:  1 0 1 1 1
Heights:     2 0 2 1 2
```

After processing row `2`:

``` text
Matrix row:  1 1 1 1 1
Heights:     3 1 3 2 3
```

The height of each column counts consecutive `1`s vertically, ending at
the current row.

## Approach

1.  Initialize `heights = [0] * cols`.
2.  Process the matrix one row at a time.
3.  Update each column's height:
    -   `1` → increment the height.
    -   `0` → reset the height to `0`.
4.  Find the largest rectangle in the current histogram.
5.  Update the global maximum area.

### Pseudocode

``` text
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
```

## Dry Run

For this matrix:

``` text
1 0 1 0 1
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
```

The histogram heights and best area after each row are:

  Row processed   Histogram heights     Best area for this histogram
  --------------- ------------------- ------------------------------
  `0`             `[1, 0, 1, 0, 1]`                                1
  `1`             `[2, 0, 2, 1, 2]`                                3
  `2`             `[3, 1, 3, 2, 3]`                                6
  `3`             `[4, 0, 0, 3, 0]`                                4

For row `2`, the heights are:

``` text
Heights:  3 1 3 2 3
              _______
Rectangle:    |     |
              |     |   height = 2
              +-----+
              width = 3

Area = height * width
     = 2 * 3
     = 6
```

Therefore, the maximum rectangle area across all rows is **6**.

## Code

The histogram helper uses a monotonic stack of indices. When a shorter
bar is encountered, it calculates the area of bars that can no longer
extend to the right.

``` python
def largest_rectangle_in_histogram(heights):
    stack = []
    max_area = 0
    n = len(heights)

    # The extra iteration flushes the remaining bars.
    for i in range(n + 1):
        while stack and (
            i == n or heights[stack[-1]] > heights[i]
        ):
            index = stack.pop()
            height = heights[index]

            previous_smaller = stack[-1] if stack else -1
            next_smaller = i
            width = next_smaller - previous_smaller - 1

            max_area = max(max_area, height * width)

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
            if matrix[i][j] == "1" or matrix[i][j] == 1:
                heights[j] += 1
            else:
                heights[j] = 0

        area = largest_rectangle_in_histogram(heights)
        max_area = max(max_area, area)

    return max_area


matrix = [
    ["1", "0", "1", "0", "1"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]

print(maximal_rectangle(matrix))  # 6
```

## Complexity

Let `N` be the number of rows and `M` be the number of columns.

-   **Time:** `O(N * M)`
    -   Updating heights across the matrix takes `O(N * M)`.
    -   Each histogram takes `O(M)` amortized time, repeated for `N`
        rows.
-   **Auxiliary space:** `O(M)` for the heights array and monotonic
    stack.

The input matrix is not modified.

## Takeaway

``` text
For every row:
    Update vertical heights
            ↓
    Treat heights as a histogram
            ↓
    Find largest rectangle in histogram
            ↓
    Update global maximum
```

**Maximal Rectangle = repeated Largest Rectangle in Histogram.**

Remember: `heights[j]` is the number of consecutive `1`s in column `j`
ending at the current row. It is not a conventional prefix sum.
