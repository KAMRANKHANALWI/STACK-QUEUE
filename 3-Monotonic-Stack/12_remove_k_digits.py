"""
Problem:
Given a number as a string `num` and an integer `k`,
remove exactly k digits so the remaining number is as small
as possible.

Example:
num = "1432219", k = 3
Output = "1219"


Pattern:
Greedy + Monotonic Stack

Key Observation:
The leftmost digits have the greatest impact on the number.

When a smaller digit arrives, removing a larger digit immediately
before it can make the number smaller.

Use a stack to keep the digits we've chosen so far.


Optimal Approach:
1. Traverse digits from left to right.
2. While the stack's top is greater than the current digit
   and removals remain, pop the top and decrement k.
3. Push the current digit.
4. If k is still positive after traversal, remove digits
   from the end.
5. Remove leading zeros.
6. If nothing remains, return "0".


Pseudocode:

    stack = []

    for digit in num:
        while stack and k > 0 and stack.top > digit:
            pop stack
            k -= 1

        push digit

    while k > 0:
        pop stack
        k -= 1

    result = join(stack)
    remove leading zeros

    if result is empty:
        return "0"

    return result


Dry Run:
num = "1432219", k = 3

Read digit 1:
    stack = [1], k = 3

Read digit 4:
    stack = [1, 4], k = 3

Read digit 3:
    4 > 3 → remove 4
    stack = [1, 3], k = 2

Read digit 2:
    3 > 2 → remove 3
    stack = [1, 2], k = 1

Read digit 2:
    2 is not greater than 2
    stack = [1, 2, 2], k = 1

Read digit 1:
    2 > 1 → remove one 2
    stack = [1, 2, 1], k = 0

Read digit 9:
    No removals left
    stack = [1, 2, 1, 9]

Answer = "1219"


Edge Cases:

1. k == len(num)
   All digits are removed.
   Return "0", not an empty string.

2. Leading zeros
   Example: "10200", k = 1
   Removing 1 leaves "0200".
   Remove leading zeros → "200".

3. k remains after traversal
   Example: "123456", k = 3
   Digits are increasing, so the main loop removes none.
   Remove the last three digits → "123".

4. All remaining digits are zeros
   Example: "1000", k = 1
   The result may become "000".
   Trimming leading zeros gives an empty string, so return "0".

Why use `>` and not `>=`?
If the top digit equals the current digit, removing it does not
improve the number. Save removals for a larger digit.


Complexity:
Time  → O(N), each digit is pushed and popped at most once.
Space → O(N) for the stack and result.

Takeaway:
Remove larger preceding digits when a smaller digit arrives.
If removals remain after traversal, remove from the end.
Always trim leading zeros and return "0" if the result is empty.
"""


def remove_k_digits(num, k):
    stack = []

    for digit in num:
        # Remove larger preceding digits while removals remain.
        while stack and k > 0 and stack[-1] > digit:
            stack.pop()
            k -= 1

        stack.append(digit)

    # If digits are increasing, k may still be positive.
    while k > 0:
        stack.pop()
        k -= 1

    # Remove leading zeros from the resulting number.
    result = "".join(stack).lstrip("0")

    # An empty result represents zero.
    return result if result else "0"


# Examples
if __name__ == "__main__":
    print(remove_k_digits("1432219", 3))  # "1219"
    print(remove_k_digits("10200", 1))    # "200"
    print(remove_k_digits("123456", 3))   # "123"
    print(remove_k_digits("1000", 1))     # "0"
    print(remove_k_digits("10", 2))       # "0"
