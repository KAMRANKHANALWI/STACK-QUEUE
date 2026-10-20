# Largest Rectangle in Histogram

## Problem

Given histogram bar heights, find the largest rectangular area.

Example: `heights = [2, 1, 5, 6, 2, 3]` → output `10`.

## Pattern: Monotonic Increasing Stack

For each bar, find the widest span where every bar is at least as tall
as the current bar.

-   **PSE:** Previous Smaller Element's index.
-   **NSE:** Next Smaller Element's index.

``` text
width = NSE - PSE - 1
area  = heights[i] * width
```

If no smaller element exists, use `PSE = -1` and `NSE = n`.

## Brute Force

For each bar, expand left and right while adjacent bars are greater than
or equal to its height. Calculate the resulting area and update the
maximum.

### Pseudocode

``` text
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
```

**Time:** `O(N²)`\
**Auxiliary space:** `O(1)`

## Optimal Approach

Maintain a stack of indices with increasing bar heights. When a shorter
bar appears, pop taller bars:

-   Current index is the popped bar's NSE.
-   The new stack top is its PSE, or `-1` if the stack is empty.
-   Compute `height * (NSE - PSE - 1)` and update the maximum.

After the array ends, use `n` as the NSE for all remaining bars.

### Pseudocode

``` text
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
```

### Python Code

``` python
def largest_rectangle_optimal(heights):
    n = len(heights)
    stack = []
    max_area = 0

    for i in range(n + 1):
        # i == n flushes bars without a smaller right boundary.
        while stack and (
            i == n or heights[stack[-1]] > heights[i]
        ):
            index = stack.pop()
            nse = i
            pse = stack[-1] if stack else -1

            width = nse - pse - 1
            area = heights[index] * width
            max_area = max(max_area, area)

        if i < n:
            stack.append(i)

    return max_area


heights = [2, 1, 5, 6, 2, 3]
print(largest_rectangle_optimal(heights))  # 10
```

**Time:** `O(N)` --- each index is pushed and popped at most once.\
**Auxiliary space:** `O(N)` for the stack.

## Dry Run

For height `5` at index `2`:

``` text
PSE = 1 (height 1)
NSE = 4 (height 2)
width = 4 - 1 - 1 = 2
area = 5 * 2 = 10
```

For height `6` at index `3`:

``` text
PSE = 2 (height 5)
NSE = 4 (height 2)
width = 4 - 2 - 1 = 1
area = 6 * 1 = 6
```

Largest area = `10`.

## Key Takeaway

A smaller bar limits how far a taller bar can extend. Pop the taller
bar, identify its PSE and NSE, then calculate:

``` text
area = height * (NSE - PSE - 1)
```

The monotonic stack reduces the time complexity from `O(N²)` to `O(N)`.

**Python detail:** Check `i == n` first in the `or` condition so
`heights[n]` is never accessed.
