# Monotonic Stack

A **monotonic stack** maintains elements in increasing or decreasing order.

The key question:

> Do I need the first greater/smaller element on one side?

If yes, think **monotonic stack**.

---

## 1. Next Greater Element

Need:

```text
First element to the right
that is greater than current
```

Typical pattern:

```text
Traverse right → left
Maintain decreasing stack
Pop elements that cannot be the answer
```

---

## 2. Next Smaller Element

Need:

```text
First element to the right
that is smaller than current
```

Maintain the appropriate increasing monotonic order.

---

## 3. Circular Array

For circular problems:

```text
Traverse conceptually 2N elements
```

Common technique:

```python
i % n
```

---

## 4. Previous Greater / Smaller

Same idea, but direction changes.

```text
Previous → process left → right
Next     → process right → left
```

---

## 5. Contribution Technique

Used in:

```text
Sum of Subarray Minimums
Sum of Subarray Ranges
```

Instead of generating every subarray:

```text
For each element:
    count how many subarrays use it
    as minimum / maximum
```

Usually based on:

```text
Previous boundary
+
Next boundary
```

---

## 6. Trapping Rainwater

Think in terms of:

```text
Boundary on left
+
Boundary on right
```

Can be solved using stack or two-pointer ideas.

---

## 7. Asteroid Collision

Stack represents the asteroids that have survived so far.

When a new asteroid arrives:

```text
Possible collision
    ↓
Compare magnitudes
    ↓
Destroy smaller
    ↓
Continue if necessary
```

---

## 8. Remove K Digits

Greedy + monotonic stack.

Core observation:

> If a smaller digit comes after a larger digit, removing the larger digit can improve the number.

Maintain an increasing structure while removing at most `k` digits.

---

## 9. Largest Rectangle in Histogram

For every bar:

```text
Previous Smaller
+
Next Smaller
=
Maximum width
```

Then:

```text
area = height × width
```

---

## 10. Maximal Rectangle

Convert each matrix row into histogram heights.

```text
Matrix
  ↓
Histogram for each row
  ↓
Largest Rectangle in Histogram
```

---

## Problems

1. Next Greater Element
2. Next Greater Element II
3. Next Smaller Element
4. Number of Greater Elements to the Right
5. Trapping Rainwater
6. Sum of Subarray Minimums
7. Asteroid Collision
8. Sum of Subarray Ranges
9. Remove K Digits
10. Largest Rectangle in Histogram
11. Maximal Rectangle

---

## Key Takeaway

```text
Next Greater / Smaller
        ↓
Monotonic Stack
        ↓
Boundaries
        ↓
Contribution
        ↓
Histogram / Subarray problems
```
