# Sum of Subarray Minimums

## Problem

Given an array, find the **sum of the minimum element of every possible
subarray**.

Example:

``` text
arr = [3, 1, 2, 4]
```

All subarrays:

``` text
[3]       → 3
[3,1]     → 1
[3,1,2]   → 1
[3,1,2,4] → 1

[1]       → 1
[1,2]     → 1
[1,2,4]   → 1

[2]       → 2
[2,4]     → 2

[4]       → 4
```

Total:

``` text
3 + 1 + 1 + 1 + 1 + 1 + 1 + 2 + 2 + 4 = 17
```

------------------------------------------------------------------------

# Core Idea

Instead of generating every subarray and finding its minimum, ask:

> **For each element `arr[i]`, in how many subarrays is `arr[i]` the
> minimum?**

Then:

``` text
answer
= contribution of arr[0]
+ contribution of arr[1]
+ ...
+ contribution of arr[n-1]
```

This is called the **Contribution Technique**.

------------------------------------------------------------------------

# The Mathematical Insight

This is where the problem becomes a little like
**permutation/combinations or the Fundamental Counting Principle**.

For an element `arr[i]`, suppose:

``` text
left choices  = L
right choices = R
```

Every valid left choice can be combined with every valid right choice.

Therefore:

``` text
number of subarrays
= L × R
```

And because `arr[i]` is the minimum in each of them:

``` text
contribution
= L × R × arr[i]
```

So the whole problem reduces to:

``` text
Find L
Find R
Multiply
```

------------------------------------------------------------------------

# Example: Why 4 × 3 = 12?

Consider:

``` text
arr = [1, 4, 6, 7, 3, 7, 8, 1]
       0  1  2  3  4  5  6  7
                   ↑
                  3
```

We focus on:

``` text
arr[4] = 3
```

We want all subarrays where `3` is the minimum.

------------------------------------------------------------------------

## 1. Find the left boundary

Look to the left of `3`:

``` text
1  4  6  7  3
↑           ↑
0           4
```

The previous smaller element is:

``` text
1 at index 0
```

So:

``` text
PSEE = 0
```

PSEE = Previous Smaller or Equal Element.

For this example there is no equal value, so it is simply the previous
smaller element.

### What does PSEE = 0 mean?

We cannot start at index `0`.

Why?

``` text
[1, 4, 6, 7, 3]
```

has minimum `1`, not `3`.

Therefore valid starting positions are:

``` text
1, 2, 3, 4
```

That's:

``` text
4 choices
```

Formula:

``` text
left = i - PSEE
     = 4 - 0
     = 4
```

------------------------------------------------------------------------

# 2. Physically see the 4 starting choices

Start at index `4`:

``` text
[3]
```

Minimum = `3` ✓

Start at index `3`:

``` text
[7, 3]
```

Minimum = `3` ✓

Start at index `2`:

``` text
[6, 7, 3]
```

Minimum = `3` ✓

Start at index `1`:

``` text
[4, 6, 7, 3]
```

Minimum = `3` ✓

Start at index `0`:

``` text
[1, 4, 6, 7, 3]
```

Minimum = `1` ✗

Therefore:

``` text
valid starts = {1, 2, 3, 4}

number of starts = 4
```

------------------------------------------------------------------------

# 3. Find the right boundary

Look to the right:

``` text
1  4  6  7  3  7  8  1
0  1  2  3  4  5  6  7
            ↑
            3
```

After `3`:

``` text
7 → 8 → 1
          ↑
       smaller
```

The next smaller element is:

``` text
1 at index 7
```

Therefore:

``` text
NSE = 7
```

NSE = Next Smaller Element.

We cannot include index `7`, because:

``` text
1 < 3
```

For example:

``` text
[3, 7, 8, 1]
```

has minimum `1`, not `3`.

So valid ending positions are:

``` text
4, 5, 6
```

That's:

``` text
3 choices
```

Formula:

``` text
right = NSE - i
      = 7 - 4
      = 3
```

------------------------------------------------------------------------

# 4. Why 4 × 3 = 12?

Now we have:

``` text
Starting choices:

1, 2, 3, 4

Ending choices:

4, 5, 6
```

Every valid start can be paired with every valid end.

Think of it like:

``` text
4 shirts × 3 pants
= 12 outfits
```

Same mathematical principle here:

``` text
4 starts × 3 ends
= 12 subarrays
```

------------------------------------------------------------------------

## All 12 subarrays

    Start   End Subarray
  ------- ----- -----------------
        1     4 `[4,6,7,3]`
        1     5 `[4,6,7,3,7]`
        1     6 `[4,6,7,3,7,8]`
        2     4 `[6,7,3]`
        2     5 `[6,7,3,7]`
        2     6 `[6,7,3,7,8]`
        3     4 `[7,3]`
        3     5 `[7,3,7]`
        3     6 `[7,3,7,8]`
        4     4 `[3]`
        4     5 `[3,7]`
        4     6 `[3,7,8]`

Count:

``` text
3 + 3 + 3 + 3
= 12
```

Or directly:

``` text
4 × 3 = 12
```

------------------------------------------------------------------------

# 5. Why does 12 become 36?

We found:

``` text
12 subarrays
```

where `3` is the minimum.

Each of those subarrays contributes:

``` text
3
```

So:

``` text
contribution of 3
= 12 × 3
= 36
```

Or directly:

``` text
contribution
= left × right × arr[i]

= 4 × 3 × 3

= 36
```

This is the key calculation.

------------------------------------------------------------------------

# 6. The Complete Mental Picture

``` text
                arr[i] = 3
                     ↓

PSEE = 0        3        NSE = 7
   ↓             ↓            ↓

valid starts             valid ends
1, 2, 3, 4               4, 5, 6
    ↓                         ↓
4 choices                 3 choices
    └──────────┬──────────────┘
               ↓
             4 × 3
               ↓
              12
               ↓
       each contributes 3
               ↓
            12 × 3
               ↓
              36
```

------------------------------------------------------------------------

# 7. General Formula

For every index `i`:

``` text
left_choices
= i - PSEE[i]

right_choices
= NSE[i] - i
```

Therefore:

``` text
number of subarrays where arr[i] is minimum
=
(i - PSEE[i]) × (NSE[i] - i)
```

Contribution:

``` text
=
(i - PSEE[i])
×
(NSE[i] - i)
×
arr[i]
```

------------------------------------------------------------------------

# 8. Why PSEE and NSE Are Enough

We don't need to explicitly generate all subarrays.

We only need the two boundaries:

``` text
PSEE[i] → where we are blocked on the left
NSE[i]  → where we are blocked on the right
```

For `3`:

``` text
PSEE = 0
i    = 4
NSE  = 7
```

Therefore:

``` text
left  = 4 - 0 = 4
right = 7 - 4 = 3

count = 4 × 3 = 12

contribution = 12 × 3 = 36
```

That is the entire trick.

------------------------------------------------------------------------

# 9. Why Monotonic Stack?

The mathematical counting is easy **once we know PSEE and NSE**.

The difficult part is finding those boundaries efficiently.

A brute-force approach could search left and right for every element:

``` text
For every i:
    find previous smaller/equal
    find next smaller
```

That can take:

``` text
O(N²)
```

A monotonic stack finds the boundaries in:

``` text
O(N)
```

So the problem combines two ideas:

``` text
Monotonic Stack
      ↓
Find PSEE and NSE
      ↓
Counting Principle
      ↓
left × right
      ↓
Contribution Technique
      ↓
left × right × arr[i]
```

------------------------------------------------------------------------

# 10. PSEE vs NSE

For the minimum contribution:

``` text
PSEE = Previous Smaller or Equal Element
NSE  = Next Smaller Element
```

Typical boundary convention:

``` text
PSEE → pop while stack_top > current
NSE  → pop while stack_top >= current
```

This asymmetric handling of equality is important when duplicate values
exist.

It ensures that equal elements are assigned consistently and prevents
counting the same subarray more than once.

------------------------------------------------------------------------

# 11. A Smaller Example

Consider:

``` text
arr = [3, 1, 2, 4]
```

Take:

``` text
arr[2] = 2
```

Previous smaller/equal:

``` text
1 at index 1
```

So:

``` text
PSEE = 1
```

Next smaller:

``` text
none
```

Use:

``` text
NSE = n = 4
```

Therefore:

``` text
left = 2 - 1 = 1
right = 4 - 2 = 2
```

So there are:

``` text
1 × 2 = 2
```

subarrays where `2` is the minimum:

``` text
[2]
[2,4]
```

Contribution:

``` text
2 × 2 = 4
```

------------------------------------------------------------------------

# 12. Connection to Mathematics

The most useful mental model is:

``` text
          DSA
           │
           ↓
   Find boundaries
           │
           ↓
     PSEE / NSE
           │
           ↓
    Count choices
           │
           ↓
      L × R
           │
           ↓
   Count × value
           │
           ↓
     Contribution
```

So yes --- this problem has a strong **combinatorics /
counting-principle feel**.

It is not really a permutation problem because we are not arranging
objects.

It is closer to the:

> **Fundamental Counting Principle**

If there are:

``` text
L independent valid choices for the left boundary
R independent valid choices for the right boundary
```

then:

``` text
L × R
```

valid `(start, end)` pairs exist.

That is exactly why:

``` text
4 × 3 = 12
```

------------------------------------------------------------------------

# 13. Final Takeaway

Don't memorize:

``` text
(i - PSEE) × (NSE - i)
```

Understand where it comes from:

``` text
PSEE
 ↓
number of possible starts

NSE
 ↓
number of possible ends

starts × ends
 ↓
number of subarrays

number of subarrays × arr[i]
 ↓
contribution of arr[i]
```

The formula is simply:

``` text
contribution of arr[i]
=
(i - PSEE[i])
×
(NSE[i] - i)
×
arr[i]
```

### One-line mental model

> **For each element: find how far it can expand left and right, count
> all `(start, end)` pairs, then multiply by the element's value.**

------------------------------------------------------------------------

## Quick Revision Card

``` text
SUM OF SUBARRAY MINIMUMS

Goal:
    Sum minimum of every subarray.

For each arr[i]:

    PSEE = previous smaller/equal index
    NSE  = next smaller index

    left  = i - PSEE
    right = NSE - i

    number of subarrays
        = left × right

    contribution
        = left × right × arr[i]

Why left × right?
    Fundamental Counting Principle:
    every valid start can pair with
    every valid end.

Pattern:
    Monotonic Stack
        +
    Contribution Technique
        +
    Counting Principle

Complexity:
    Time  → O(N)
    Space → O(N)
```
