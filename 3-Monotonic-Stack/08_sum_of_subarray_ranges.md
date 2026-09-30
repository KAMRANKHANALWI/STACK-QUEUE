# Sum of Subarray Ranges

## Problem

Given an array, find the sum of the **range of every subarray**.

Range of a subarray:

```text
range = maximum - minimum
```

Example:

```text
arr = [1, 4, 3, 2]
```

Output:

```text
13
```

---

## Key Observation

Instead of calculating the range of every subarray separately:

```text
Sum of Ranges
=
Sum of Subarray Maximums
-
Sum of Subarray Minimums
```

So the problem becomes two contribution problems:

```text
Sum of Maximums
        -
Sum of Minimums
```

---

## Pattern

```text
Monotonic Stack
+
Contribution Technique
```

The same idea used in:

```text
07_sum_of_subarray_minimums.py
```

is used here twice:

```text
Minimum contribution
+
Maximum contribution
```

---

## Brute Force

Generate every subarray.

While extending the subarray, maintain:

```text
largest
smallest
```

Then:

```text
range = largest - smallest
```

### Pseudocode

```text
sum = 0

for i = 0 → n-1:

    largest = arr[i]
    smallest = arr[i]

    for j = i+1 → n-1:

        largest = max(largest, arr[j])
        smallest = min(smallest, arr[j])

        sum += largest - smallest

return sum
```

### Complexity

```text
Time  → O(N²)
Space → O(1)
```

---

# Optimal Approach

For every subarray:

```text
range = maximum - minimum
```

Therefore:

```text
Σ range
=
Σ maximum - Σ minimum
```

So calculate:

```text
sum_max = Sum of Subarray Maximums
sum_min = Sum of Subarray Minimums
```

Finally:

```text
answer = sum_max - sum_min
```

---

# 1. Sum of Subarray Minimums

For every `arr[i]`, find how many subarrays have `arr[i]`
as their minimum.

Use:

```text
PSEE → Previous Smaller OR Equal
NSE  → Next Strictly Smaller
```

Then:

```text
left  = i - PSEE[i]
right = NSE[i] - i
```

Number of subarrays where `arr[i]` is minimum:

```text
left × right
```

Contribution:

```text
left × right × arr[i]
```

Therefore:

```text
sum_min =
Σ ((i - PSEE[i])
× (NSE[i] - i)
× arr[i])
```

---

# 2. Sum of Subarray Maximums

Same idea, but now we count subarrays where `arr[i]`
is the maximum.

Use:

```text
PGE → Previous Greater OR Equal
NGE → Next Strictly Greater
```

Then:

```text
left  = i - PGE[i]
right = NGE[i] - i
```

Contribution:

```text
left × right × arr[i]
```

Therefore:

```text
sum_max =
Σ ((i - PGE[i])
× (NGE[i] - i)
× arr[i])
```

---

# Duplicate Handling

Use asymmetric comparisons so equal elements are not
counted twice.

### Minimum

```text
PSEE:
    pop while arr[stack[-1]] > arr[i]

NSE:
    pop while arr[stack[-1]] >= arr[i]
```

### Maximum

```text
PGE:
    pop while arr[stack[-1]] < arr[i]

NGE:
    pop while arr[stack[-1]] <= arr[i]
```

---

# Example

```text
arr = [1, 4, 3, 2]
```

All subarrays:

```text
[1]         → max=1, min=1 → 0

[1,4]       → 4 - 1 = 3
[1,4,3]     → 4 - 1 = 3
[1,4,3,2]   → 4 - 1 = 3

[4]         → 0
[4,3]       → 4 - 3 = 1
[4,3,2]     → 4 - 2 = 2

[3]         → 0
[3,2]       → 3 - 2 = 1

[2]         → 0
```

Therefore:

```text
0 + 3 + 3 + 3
+ 0 + 1 + 2
+ 0 + 1
+ 0

= 13
```

---

# The Mathematical Connection

This problem is basically:

```text
Range = Maximum - Minimum
```

So:

```text
Sum of Ranges
=
Σ(Maximum - Minimum)

=
Σ Maximum - Σ Minimum
```

This allows us to separate the problem into two
independent contribution calculations.

---

# Core Formula

For minimum:

```text
PSEE ← arr[i] → NSE

left  = i - PSEE
right = NSE - i

contribution =
left × right × arr[i]
```

For maximum:

```text
PGE ← arr[i] → NGE

left  = i - PGE
right = NGE - i

contribution =
left × right × arr[i]
```

Finally:

```text
answer = sum_max - sum_min
```

---

# Complexity

### Brute

```text
Time  → O(N²)
Space → O(1)
```

### Optimal

```text
Find PSEE/NSE → O(N)
Find PGE/NGE  → O(N)

Total Time  → O(N)
Space       → O(N)
```

---

# Takeaway

The entire problem reduces to:

```text
Range
=
Maximum - Minimum
```

Therefore:

```text
Sum of Subarray Ranges
=
Sum of Subarray Maximums
-
Sum of Subarray Minimums
```

And both are solved using the same idea:

```text
Monotonic Stack
        ↓
Find boundaries
        ↓
Count left × right choices
        ↓
Calculate contribution
```

### Mental Model

```text
MINIMUM

PSEE ← element → NSE
        ↓
left × right × element


MAXIMUM

PGE ← element → NGE
        ↓
left × right × element
```

So remember:

```text
SUM OF RANGES
      =
SUM OF MAX
      -
SUM OF MIN
```

This is essentially the **Sum of Subarray Minimums technique applied twice**.
