
"""
Problem:
Given an array and window size k, return the maximum
element from every contiguous window of size k.

Example:
nums = [1, 3, -1, -3, 5, 3, 7, 1, 6]
k = 3

Output:
[3, 3, 5, 5, 7, 7, 7]


Pattern:
Sliding Window + Monotonic Deque


--------------------------------------------------
Brute Force
--------------------------------------------------

Approach:
For every window:
1. Traverse its k elements.
2. Find the maximum.
3. Append it to the answer.

Pseudocode:

    for i from 0 to n-k:

        maximum = nums[i]

        for j from i to i+k-1:
            maximum = max(maximum, nums[j])

        answer.append(maximum)

Complexity:
Time  → O((N-K+1) * K) = O(NK)
Space → O(1), excluding output.


--------------------------------------------------
Optimal — Monotonic Deque
--------------------------------------------------

Key Observation:
We only need elements that can potentially become
the maximum of the current or future windows.

Maintain a decreasing deque of indices.

Deque:
- Front → index of maximum element
- Back  → smaller/equal elements to remove

Rules:
1. Remove expired indices from the front.
2. Remove smaller/equal elements from the back.
3. Push the current index.
4. Once the window is complete, add the front value.

Pseudocode:

    create deque
    create answer list

    for i from 0 to n-1:

        remove indices outside current window

        while deque is not empty AND
              nums[deque.back] <= nums[i]:
            remove from back

        push i into deque

        if i >= k-1:
            answer.append(nums[deque.front])

    return answer

Complexity:
Time  → O(N)
Space → O(K)

Why O(N)?
Every index enters the deque once and leaves it
at most once.


Takeaway:
Brute Force → Check every element in every window.

Optimal → Maintain only useful candidates using
          a Monotonic Deque.

Front → Maximum
Back  → Smaller elements
"""

from collections import deque


# --------------------------------------------------
# Brute Force
# --------------------------------------------------

def max_sliding_window_brute(nums, k):
    n = len(nums)
    answer = []

    for i in range(n - k + 1):

        maximum = nums[i]

        # Check all k elements in the current window
        for j in range(i, i + k):
            maximum = max(maximum, nums[j])

        answer.append(maximum)

    return answer


# --------------------------------------------------
# Optimal — Monotonic Deque
# --------------------------------------------------

def max_sliding_window_optimal(nums, k):
    dq = deque()  # Stores indices
    answer = []

    for i in range(len(nums)):

        # 1. Remove indices outside the current window
        while dq and dq[0] <= i - k:
            dq.popleft()

        # 2. Maintain decreasing order
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()

        # 3. Add current index
        dq.append(i)

        # 4. Record maximum once window is complete
        if i >= k - 1:
            answer.append(nums[dq[0]])

    return answer


# --------------------------------------------------
# Example
# --------------------------------------------------

nums = [1, 3, -1, -3, 5, 3, 7, 1, 6]
k = 3

print("Brute:  ", max_sliding_window_brute(nums, k))
print("Optimal:", max_sliding_window_optimal(nums, k))

# Brute:   [3, 3, 5, 5, 7, 7, 7]
# Optimal: [3, 3, 5, 5, 7, 7, 7]
