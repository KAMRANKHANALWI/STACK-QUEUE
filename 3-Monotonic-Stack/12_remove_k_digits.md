# 12. Remove K Digits

## Problem

Given a number as a string `num` and an integer `k`, remove exactly `k`
digits so that the remaining number is as small as possible.

``` text
num = "1432219"
k = 3

Output: "1219"
```

## Pattern

**Greedy + Monotonic Stack**

Keep smaller digits toward the beginning. When a smaller digit arrives,
remove larger digits immediately before it, as long as removals remain.

## Key Intuition

The leftmost digits matter most. For example, `13` is smaller than `14`.
So if we have kept `14` and the next digit is `3`, removing `4` lets us
keep `13`, which is better.

A stack works because we only need to reconsider the most recently kept
digit.

## Optimal Approach

For each digit in `num`:

1.  While the stack is not empty, `k > 0`, and the top digit is greater
    than the current digit:
    -   Pop the top digit.
    -   Decrease `k`.
2.  Push the current digit.
3.  After processing every digit, if `k` is still greater than `0`,
    remove that many digits from the end.
4.  Remove leading zeros.
5.  If nothing remains, return `"0"`.

### Pseudocode

``` text
stack = []

for digit in num:
    while stack is not empty
          and k > 0
          and stack.top > digit:
        pop stack
        k -= 1

    push digit

while k > 0:
    pop stack
    k -= 1

result = join(stack)
remove leading zeros from result

if result is empty:
    return "0"

return result
```

## Dry Run

``` text
num = "1432219"
k = 3
```

Read digits from left to right.

  Current digit   What happens                             Stack after processing     `k` left
  --------------- ---------------------------------------- ------------------------ ----------
  `1`             Stack is empty; push `1`                 `1`                               3
  `4`             `4` is larger than `1`; keep it          `14`                              3
  `3`             `4 > 3`; remove `4`, then push `3`       `13`                              2
  `2`             `3 > 2`; remove `3`, then push `2`       `12`                              1
  `2`             `2` is not greater than `2`; push it     `122`                             1
  `1`             `2 > 1`; remove one `2`, then push `1`   `121`                             0
  `9`             No removals left; push `9`               `1219`                            0

Final answer: `"1219"`.

### Why use `>` and not `>=`?

When the top digit equals the current digit, removing the top digit does
not make the number smaller. Save the limited removals for a digit that
can improve the result.

## Edge Cases 

### 1. `k` equals the number of digits

``` text
num = "1000"
k = 4
```

We must remove all four digits, leaving nothing. The answer should be
represented as `"0"`, not an empty string.

``` text
Output: "0"
```

The code handles this with the final check: if the result is empty,
return `"0"`.

### 2. The result begins with zeros

``` text
num = "10200"
k = 1
```

The best removal is `1`, leaving `"0200"`. Leading zeros do not change
the number's value, so the standard representation is `"200"`.

``` text
Output: "200"
```

Use `lstrip("0")` to remove zeros from the **beginning** of the result.

### 3. Removals are left after reading every digit

``` text
num = "123456"
k = 3
```

The digits are already in increasing order, so the main loop never needs
to remove one. But we still must remove exactly three digits.

``` text
1 2 3 4 5 6
      └──── remove 4, 5, 6

Result: "123"
```

When digits increase from left to right, removing from the end gives the
smallest result. That is why we need the final `while k > 0` loop.

### 4. All remaining digits are zeros

``` text
num = "1000"
k = 1
```

The process can leave `"000"`. After leading zeros are removed, the
string becomes empty. The correct numeric result is `"0"`.

This is covered by the same final empty-result check.

### Edge Cases at a Glance

  -----------------------------------------------------------------------
  Situation               Why it matters          Required handling
  ----------------------- ----------------------- -----------------------
  `k == len(num)`         Every digit is removed  Return `"0"`

  Leading zeros           `"0200"` is represented Use `lstrip("0")`
                          as `"200"`              

  `k > 0` after traversal The main loop did not   Pop from the end
                          use every removal       

  Result is empty after   No digits remain, or    Return `"0"`
  trimming                all were zero           
  -----------------------------------------------------------------------

## Code

``` python
def remove_k_digits(num, k):
    stack = []

    for digit in num:
        # Remove larger preceding digits to make the number smaller.
        while stack and k > 0 and stack[-1] > digit:
            stack.pop()
            k -= 1

        stack.append(digit)

    # If digits are increasing, removals may remain.
    while k > 0:
        stack.pop()
        k -= 1

    # Remove leading zeros from the remaining number.
    result = "".join(stack).lstrip("0")

    # Empty means no digits remain or all remaining digits were zero.
    return result if result else "0"


# Examples
print(remove_k_digits("1432219", 3))  # "1219"
print(remove_k_digits("10200", 1))    # "200"
print(remove_k_digits("123456", 3))   # "123"
print(remove_k_digits("1000", 1))     # "0"
print(remove_k_digits("10", 2))       # "0"
```

## Complexity

Let `N = len(num)`.

-   **Time:** `O(N)`. Each digit is pushed once and popped at most once.
-   **Auxiliary space:** `O(N)` for the stack and result.

## Takeaway

``` text
Smaller current digit arrives
          ↓
Remove larger digits from stack
while k > 0
          ↓
Push current digit
          ↓
Remove leftover k digits from the end
          ↓
Trim leading zeros
          ↓
If empty, return "0"
```

**Remember:** Greedily remove a larger digit when a smaller digit
arrives. If removals remain at the end, remove from the right.
