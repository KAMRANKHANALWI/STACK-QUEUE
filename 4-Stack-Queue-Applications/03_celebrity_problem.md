# Celebrity Problem

## Problem

Given an `N x N` matrix, find the celebrity.

A celebrity: 1. Is known by everyone else. 2. Knows nobody else.

``` text
mat[i][j] = 1  → Person i knows person j
mat[i][j] = 0  → Person i does not know person j
```

Ignore the diagonal (`mat[i][i]`).

------------------------------------------------------------------------

## Pattern

**Matrix Traversal + Two-Pointer Elimination**

### Key Observation

For person `x` to be a celebrity:

-   Row `x` must contain only `0`s (excluding the diagonal).
-   Column `x` must contain only `1`s (excluding the diagonal).

``` text
Celebrity's row    → all 0s
Celebrity's column → all 1s
```

------------------------------------------------------------------------

## 1. Brute Force

Maintain two arrays:

-   `knows_me[i]`: number of people who know person `i`.
-   `i_know[i]`: number of people person `i` knows.

For every `1` at `mat[i][j]`:

``` text
i_know[i] += 1
knows_me[j] += 1
```

A person is a celebrity when:

``` text
i_know[i] == 0
knows_me[i] == n - 1
```

### Pseudocode

``` text
create knows_me and i_know arrays

for i from 0 to n - 1:
    for j from 0 to n - 1:

        if i != j and mat[i][j] == 1:
            i_know[i] += 1
            knows_me[j] += 1

for i from 0 to n - 1:
    if i_know[i] == 0 and knows_me[i] == n - 1:
        return i

return -1
```

### Complexity

-   Time: `O(N²)` --- inspect every matrix cell.
-   Space: `O(N)` --- two auxiliary arrays.

------------------------------------------------------------------------

## 2. Optimal --- Two-Pointer Elimination

Eliminate people who cannot be celebrities.

Initialize:

``` text
top = 0
down = n - 1
```

Compare the two people:

### Case 1: `mat[top][down] == 1`

`top` knows `down`, so `top` cannot be the celebrity.

``` text
top += 1
```

### Case 2: `mat[down][top] == 1`

`down` knows `top`, so `down` cannot be the celebrity.

``` text
down -= 1
```

### Case 3: Neither knows the other

``` text
mat[top][down] == 0
mat[down][top] == 0
```

-   `top` cannot be the celebrity because `down` does not know `top`.
-   `down` cannot be the celebrity because `top` does not know `down`.

Eliminate both:

``` text
top += 1
down -= 1
```

After elimination:

-   If `top > down`, no candidate remains.
-   Otherwise, `top` is the only possible candidate.

### Verification

Elimination gives only a *candidate*. Verify it:

-   Candidate's row must contain only `0`s (excluding itself).
-   Candidate's column must contain only `1`s (excluding itself).

### Pseudocode

``` text
top = 0
down = n - 1

while top < down:

    if mat[top][down] == 1:
        top += 1

    elif mat[down][top] == 1:
        down -= 1

    else:
        top += 1
        down -= 1

if top > down:
    return -1

candidate = top

for i from 0 to n - 1:

    if i == candidate:
        continue

    if mat[candidate][i] == 1:
        return -1

    if mat[i][candidate] == 0:
        return -1

return candidate
```

### Complexity

-   Elimination: `O(N)`.
-   Verification: `O(N)`.
-   **Total time: `O(N)`.**
-   **Auxiliary space: `O(1)`.**

------------------------------------------------------------------------

## Dry Run

``` python
mat = [
    [0, 1, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]
```

Initially:

``` text
top = 0
down = 3
```

  -----------------------------------------------------------------------
  Check                   Observation             Action
  ----------------------- ----------------------- -----------------------
  `mat[0][3] = 0`,        Person 3 knows person 0 `down = 2`
  `mat[3][0] = 1`                                 

  `mat[0][2] = 1`         Person 0 knows person 2 `top = 1`

  `mat[1][2] = 0`,        Person 2 knows person 1 `down = 1`
  `mat[2][1] = 1`                                 
  -----------------------------------------------------------------------

Candidate: `1`

Verify person 1:

``` text
Row 1    → [0, 0, 0, 0]
Column 1 → [1, 0, 1, 1]
```

Everyone else knows person 1, and person 1 knows nobody.

**Answer: `1`**

------------------------------------------------------------------------

## Takeaway

  Approach                       Time    Space
  ------------------------- --------- --------
  Brute Force                 `O(N²)`   `O(N)`
  Two-Pointer Elimination      `O(N)`   `O(1)`

Remember:

-   If `A` knows `B`, `A` cannot be the celebrity.
-   If `A` does not know `B`, `B` cannot be the celebrity.
-   Elimination finds a candidate; verification confirms it.
