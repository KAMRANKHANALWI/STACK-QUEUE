"""
Problem:
Given an array and Q query indices, find the number of
elements strictly greater than arr[index] on its right.

Example:
arr     = [5, 2, 10, 4]
queries = [0, 1]

Output:
[1, 2]


Pattern:
Query-based array traversal.

Important:
Unlike Next Greater Element, we are NOT looking for
the first/nearest greater element.

We need to COUNT ALL greater elements on the right.


Brute Force:
For every query index:

    1. Get arr[index].
    2. Traverse from index + 1 to n - 1.
    3. Count elements greater than arr[index].


Pseudocode — Brute:

    for each index in queries:
        count = 0

        for j from index + 1 to n - 1:
            if arr[j] > arr[index]:
                count += 1

        add count to answer


Complexity — Brute:
For each query → O(N)
For Q queries   → O(Q × N)

Space → O(Q) for the answer.


Why not a normal Monotonic Stack?

A monotonic stack is excellent when we need:

    "What is the FIRST greater element?"

Here we need:

    "How MANY elements are greater?"

A stack removes elements that may still matter for counting,
so the normal NGE monotonic-stack pattern does not directly
solve this problem.


Optimized:
Precompute the count of greater elements to the right
for EVERY index using a Fenwick Tree (Binary Indexed Tree).

Traverse from right → left.

The Fenwick Tree stores the frequency of values already
seen on the right.

For arr[i]:

    greater = elements_seen - elements_<=_arr[i]

Coordinate compression is used because array values can
be large.


Pseudocode — Optimized:

    compress all values into ranks

    create Fenwick Tree
    count_greater = [0] * n
    elements_seen = 0

    for i from n - 1 down to 0:

        rank = compressed_rank(arr[i])

        <= current = fenwick.query(rank)

        count_greater[i] = elements_seen - <= current

        fenwick.add(rank, 1)

        elements_seen += 1

    answer = [count_greater[index] for index in queries]


Complexity — Optimized:

    Coordinate compression → O(N log N)
    Fenwick processing    → O(N log N)
    Answer queries         → O(Q)

Total → O(N log N + Q)

Space → O(N)


Dry Run:

arr = [5, 2, 10, 4]

Traverse from right:

4:
    right elements = []
    greater = 0

10:
    right = [4]
    greater than 10 = 0

2:
    right = [10, 4]
    greater than 2 = 2

5:
    right = [2, 10, 4]
    greater than 5 = 1

count_greater =
[1, 2, 0, 0]

queries = [0, 1]

answer =
[1, 2]


Takeaway:

Number of Greater Elements to Right ≠ Next Greater Element.

NGE:
    Find FIRST greater element.

This problem:
    COUNT ALL greater elements.

For the original TUF constraints:
    O(Q × N) brute force is sufficient.

For a more general optimized solution:
    Fenwick Tree + Coordinate Compression
    → O(N log N + Q)
"""


# --------------------------------------------------
# Brute Force
# --------------------------------------------------

def count_greater_brute(arr, queries):
    answer = []

    for index in queries:
        count = 0

        # Check every element to the right
        for j in range(index + 1, len(arr)):

            if arr[j] > arr[index]:
                count += 1

        answer.append(count)

    return answer


# --------------------------------------------------
# Fenwick Tree
# --------------------------------------------------

class FenwickTree:
    def __init__(self, n):
        self.tree = [0] * (n + 1)

    def add(self, index, value):
        while index < len(self.tree):
            self.tree[index] += value
            index += index & -index

    def query(self, index):
        total = 0

        while index > 0:
            total += self.tree[index]
            index -= index & -index

        return total


# --------------------------------------------------
# Optimized
# --------------------------------------------------

def count_greater_optimal(arr, queries):
    n = len(arr)

    # Coordinate compression
    values = sorted(set(arr))

    rank = {
        value: i + 1
        for i, value in enumerate(values)
    }

    fenwick = FenwickTree(len(values))

    # count_greater[i] =
    # number of elements greater than arr[i] on its right
    count_greater = [0] * n

    elements_seen = 0

    # Traverse from right → left
    for i in range(n - 1, -1, -1):

        current_rank = rank[arr[i]]

        # Number of elements <= arr[i]
        less_or_equal = fenwick.query(current_rank)

        # Everything else is strictly greater
        count_greater[i] = elements_seen - less_or_equal

        # Add current element for future elements
        fenwick.add(current_rank, 1)

        elements_seen += 1

    # Answer only the requested indices
    return [count_greater[index] for index in queries]


# --------------------------------------------------
# Example
# --------------------------------------------------

arr = [5, 2, 10, 4]
queries = [0, 1]

print("Brute:   ", count_greater_brute(arr, queries))
print("Optimal: ", count_greater_optimal(arr, queries))