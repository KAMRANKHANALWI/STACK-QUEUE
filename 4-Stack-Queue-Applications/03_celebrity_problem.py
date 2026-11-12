
"""
Problem:
Given an N x N matrix, find the celebrity.

Celebrity:
1. Everyone knows the celebrity.
2. The celebrity knows no one.

Matrix:
    mat[i][j] = 1 → Person i knows person j
    mat[i][j] = 0 → Person i does not know person j

Pattern:
Matrix Traversal + Two-Pointer Elimination

Key Observation:
For a person x to be a celebrity:

    Row x → all 0s (knows nobody)
    Column x → all 1s (everyone knows x)

Ignore the diagonal: mat[x][x].


--------------------------------------------------
Brute Force
--------------------------------------------------

Maintain two arrays:

    knows_me[i] → number of people who know person i
    i_know[i]   → number of people person i knows

For every matrix cell containing 1:

    i_know[i] += 1
    knows_me[j] += 1

A celebrity must satisfy:

    i_know[i] == 0
    knows_me[i] == n - 1

Pseudocode:

    create knows_me and i_know arrays

    for i from 0 to n-1:
        for j from 0 to n-1:

            if i != j and mat[i][j] == 1:
                i_know[i] += 1
                knows_me[j] += 1

    for i from 0 to n-1:
        if i_know[i] == 0 and knows_me[i] == n-1:
            return i

    return -1

Complexity:
Time  → O(N²)
Space → O(N)


--------------------------------------------------
Optimal — Two-Pointer Elimination
--------------------------------------------------

Initially:

    top  = 0
    down = n - 1

Compare two people:

1. If mat[top][down] == 1:
       top knows down
       → top cannot be celebrity
       → top += 1

2. Else if mat[down][top] == 1:
       down knows top
       → down cannot be celebrity
       → down -= 1

3. Otherwise:
       neither knows the other
       → both cannot be celebrity
       → top += 1
       → down -= 1

After elimination:

    If top > down:
        No celebrity exists.

    Otherwise:
        top is the only possible candidate.


Verification:
A candidate must satisfy:

    Candidate's row → all 0s
    Candidate's column → all 1s

Ignore the diagonal.


Pseudocode — Optimal:

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

    for i from 0 to n-1:

        if i == candidate:
            continue

        if mat[candidate][i] == 1:
            return -1

        if mat[i][candidate] == 0:
            return -1

    return candidate


Complexity:
Elimination → O(N)
Verification → O(N)

Total Time → O(N)
Space      → O(1)


Dry Run:

mat =
[
    [0, 1, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

Initial:
top = 0, down = 3

mat[0][3] = 0
mat[3][0] = 1

Person 3 knows person 0.
Person 3 cannot be celebrity.

down = 2

mat[0][2] = 1

Person 0 knows person 2.
Person 0 cannot be celebrity.

top = 1

mat[1][2] = 0
mat[2][1] = 1

Person 2 knows person 1.
Person 2 cannot be celebrity.

down = 1

Candidate = 1

Verify:
Row 1 → [0, 0, 0, 0]
Column 1 → [1, 0, 1, 1]

Everyone knows person 1.
Person 1 knows nobody.

Answer = 1


Takeaway:

Brute Force:
    Count incoming and outgoing connections.

Optimal:
    Eliminate impossible candidates using two pointers.
    Verify the remaining candidate.

Key Rule:
    If A knows B → A cannot be celebrity.
    If A does not know B → B cannot be celebrity.
"""


# --------------------------------------------------
# Brute Force
# --------------------------------------------------

def celebrity_brute(mat):
    n = len(mat)

    knows_me = [0] * n
    i_know = [0] * n

    # Count incoming and outgoing connections
    for i in range(n):
        for j in range(n):

            if i != j and mat[i][j] == 1:
                i_know[i] += 1
                knows_me[j] += 1

    # Find person who knows nobody
    # and is known by everyone else
    for i in range(n):

        if i_know[i] == 0 and knows_me[i] == n - 1:
            return i

    return -1


# --------------------------------------------------
# Optimal — Two-Pointer Elimination
# --------------------------------------------------

def celebrity_optimal(mat):
    n = len(mat)

    if n == 0:
        return -1

    top = 0
    down = n - 1

    # Step 1: Eliminate impossible candidates
    while top < down:

        if mat[top][down] == 1:
            # top knows down → top cannot be celebrity
            top += 1

        elif mat[down][top] == 1:
            # down knows top → down cannot be celebrity
            down -= 1

        else:
            # Neither knows the other → eliminate both
            top += 1
            down -= 1

    # No candidate remains
    if top > down:
        return -1

    candidate = top

    # Step 2: Verify the candidate
    for i in range(n):

        if i == candidate:
            continue

        # Celebrity must know nobody
        if mat[candidate][i] == 1:
            return -1

        # Everybody must know the celebrity
        if mat[i][candidate] == 0:
            return -1

    return candidate


# --------------------------------------------------
# Example
# --------------------------------------------------

mat = [
    [0, 1, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

print("Brute:  ", celebrity_brute(mat))
print("Optimal:", celebrity_optimal(mat))

# Brute:   1
# Optimal: 1
