"""
Problem:
Design a Stack that supports:

- push(x)
- pop()
- top()
- get_min()

All operations should run in O(1).

Pattern:
Stack + Minimum Tracking

Key Observation:
A normal Stack cannot give the minimum in O(1).

If we scan the whole stack for every get_min():
    O(N)

So we need to store enough information while pushing
to know the current minimum immediately.

------------------------------------------------------------
Approach 1: Store (value, minimum_so_far)
------------------------------------------------------------

Instead of storing only:

    value

store:

    (value, minimum_so_far)

Example:

push(12) → (12, 12)
push(15) → (15, 12)
push(10) → (10, 10)

Stack:

    (12, 12)
    (15, 12)
    (10, 10)

get_min() → top pair's minimum → 10

After popping (10, 10):

    (12, 12)
    (15, 12)

get_min() → 12

This is very easy to understand.

Complexity:
push   → O(1)
pop    → O(1)
top    → O(1)
get_min → O(1)

Space:
O(N) pairs

------------------------------------------------------------
Approach 2: Optimized — Store only ONE value
------------------------------------------------------------

We want to avoid storing:

    (value, minimum)

Instead, store only one number.

Normal case:
If value >= current minimum:

    push(value)

The minimum does not change.

Example:

    min = 12
    value = 15

Since:

    15 >= 12

Simply store:

    15

------------------------------------------------------------
The Special Case
------------------------------------------------------------

If:

    value < current minimum

then the minimum changes.

Example:

    previous minimum = 12
    new value = 10

If we simply store 10, after popping it we would
not know that the previous minimum was 12.

So we store an encoded value:

    encoded = 2 * value - previous_minimum

For:

    value = 10
    previous_minimum = 12

    encoded = 2 * 10 - 12
            = 20 - 12
            = 8

So instead of storing 10:

    push(8)

and update:

    minimum = 10

------------------------------------------------------------
Why does this formula work?
------------------------------------------------------------

We created:

    encoded = 2 * new_minimum - previous_minimum

Example:

    8 = 2 * 10 - 12

When we later pop 8, we know:

    current minimum = 10
    encoded = 8

From:

    encoded = 2 * current_minimum - previous_minimum

we rearrange:

    previous_minimum
        = 2 * current_minimum - encoded

Therefore:

    previous_minimum
        = 2 * 10 - 8
        = 12

So the old minimum is recovered.

------------------------------------------------------------
Why is the encoded value special?
------------------------------------------------------------

When a new minimum is created:

    value < previous_minimum

Therefore:

    2 * value - previous_minimum < value

Since:

    value = current minimum

we get:

    encoded < current minimum

So:

    top < minimum

means the top is an encoded value.

This allows us to recognize the special case.

------------------------------------------------------------
Operations
------------------------------------------------------------

push(value):

If stack is empty:
    minimum = value
    push(value)

Else if value >= minimum:
    push(value)

Else:
    encoded = 2 * value - minimum
    push(encoded)
    minimum = value


top():

If stack is empty:
    return None

x = stack[-1]

If x < minimum:
    return minimum

Otherwise:
    return x


pop():

If stack is empty:
    return None

x = stack.pop()

If x < minimum:
    minimum = 2 * minimum - x


get_min():

Return minimum.


Dry Run:

push(12)

stack = [12]
minimum = 12


push(15)

15 >= 12

stack = [12, 15]
minimum = 12


push(10)

10 < 12

encoded = 2 * 10 - 12
        = 8

stack = [12, 15, 8]
minimum = 10


get_min()

→ 10


top()

top = 8

8 < 10

So 8 is encoded.

Actual top = minimum = 10

→ 10


pop()

x = 8

8 < 10

So 8 is encoded.

Recover previous minimum:

minimum = 2 * 10 - 8
        = 12


stack = [12, 15]
minimum = 12


get_min()

→ 12


top()

top = 15

15 < 12 ? No.

So actual top = 15.

→ 15


Complexity:

push    → O(1)
pop     → O(1)
top     → O(1)
get_min → O(1)

Space:
O(N)

Takeaway:
The difficult part is remembering the previous minimum
without storing another value.

When a new minimum appears:

    encoded = 2 * new_minimum - previous_minimum

Later we can recover:

    previous_minimum = 2 * current_minimum - encoded

The formula is simply algebra that lets us go
back to the previous minimum.
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.minimum = None

    def push(self, value):
        # First element
        if not self.stack:
            self.minimum = value
            self.stack.append(value)
            return

        # Normal case:
        # Minimum does not change
        if value >= self.minimum:
            self.stack.append(value)

        # New minimum → store encoded value
        else:
            encoded = 2 * value - self.minimum

            self.stack.append(encoded)
            self.minimum = value

    def pop(self):
        if not self.stack:
            return None

        x = self.stack.pop()

        # Encoded value → recover previous minimum
        if x < self.minimum:
            self.minimum = 2 * self.minimum - x

        return x

    def top(self):
        if not self.stack:
            return None

        x = self.stack[-1]

        # Encoded value means actual top is minimum
        if x < self.minimum:
            return self.minimum

        return x

    def get_min(self):
        if not self.stack:
            return None

        return self.minimum


# Example
stack = MinStack()

stack.push(12)
stack.push(15)
stack.push(10)

print(stack.get_min())  # 10

stack.pop()

print(stack.get_min())  # 12
print(stack.top())  # 15

stack.push(10)

print(stack.top())  # 10
print(stack.get_min())  # 10
