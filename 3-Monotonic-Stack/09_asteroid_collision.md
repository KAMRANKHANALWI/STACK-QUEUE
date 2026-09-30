# Asteroid Collision

## Problem

Given an array of asteroids:

- `+` → moving right
- `-` → moving left
- absolute value → asteroid size

When two asteroids moving toward each other collide:

```text
smaller  → destroyed
larger   → survives
equal    → both destroyed
```

Asteroids moving in the same direction never collide.

Example:

```text
arr = [5, 10, -5]

Output = [5, 10]
```

`10` destroys `-5`.

---

## Pattern

```text
Stack + Simulation
```

The stack stores asteroids that are still alive.

---

## Key Observation

A collision can happen **only** when:

```text
stack[-1] > 0
current  < 0
```

Why?

```text
positive → moving right
negative → moving left

→ ←
```

They move toward each other.

All other cases cannot collide:

```text
+ +
- -
- +
```

---

## Collision Rules

Suppose:

```text
top = stack[-1]
current = -x
```

### Case 1 — Top is smaller

```text
abs(top) < abs(current)
```

Then:

```text
top → destroyed
```

Pop it and keep checking.

```text
while stack and stack[-1] > 0 and abs(stack[-1]) < abs(current):
    stack.pop()
```

---

### Case 2 — Both are equal

```text
abs(top) == abs(current)
```

Both are destroyed:

```text
stack.pop()
current = 0
```

---

### Case 3 — Top is larger

```text
abs(top) > abs(current)
```

Current asteroid is destroyed:

```text
current = 0
```

---

### Case 4 — No collision

If:

```text
stack is empty
```

or:

```text
stack[-1] < 0
```

the current asteroid survives and is pushed.

---

# Pseudocode

```text
stack = []

for asteroid in arr:

    alive = True

    while alive
          and asteroid < 0
          and stack is not empty
          and stack[-1] > 0:

        if abs(stack[-1]) < abs(asteroid):
            stack.pop()

        elif abs(stack[-1]) == abs(asteroid):
            stack.pop()
            alive = False

        else:
            alive = False

    if alive:
        stack.append(asteroid)

return stack
```

---

# Dry Run

```text
arr = [4, 7, 1, 1, 2, -3, -7, 17, 15, -16]
```

Process left → right.

### `4`

```text
stack = [4]
```

### `7`

Same direction → no collision.

```text
stack = [4, 7]
```

### `1`

```text
stack = [4, 7, 1]
```

### `1`

```text
stack = [4, 7, 1, 1]
```

### `2`

```text
stack = [4, 7, 1, 1, 2]
```

### `-3`

`2` and `-3` collide:

```text
2 < 3
```

So `2` is destroyed.

Next:

```text
1 < 3
```

destroyed.

Next:

```text
1 < 3
```

destroyed.

Next:

```text
7 > 3
```

So `-3` is destroyed.

```text
stack = [4, 7]
```

---

### `-7`

Now:

```text
7 == 7
```

Both are destroyed.

```text
stack = [4]
```

---

### `17`

No collision.

```text
stack = [4, 17]
```

### `15`

Both move right → no collision.

```text
stack = [4, 17, 15]
```

### `-16`

`15 < 16`:

```text
15 → destroyed
```

Now:

```text
17 > 16
```

So `-16` is destroyed.

Final:

```text
[4, 17]
```

---

# Why Stack?

We only need to compare the current asteroid with the **nearest
surviving asteroid on its left**.

That asteroid is exactly:

```text
stack[-1]
```

If it gets destroyed, we expose the next surviving asteroid:

```text
stack.pop()
```

So the stack naturally simulates the collisions.

---

# Brute Force

A direct simulation can repeatedly scan for adjacent
collisions and remove destroyed asteroids.

This can require repeated shifting/removal.

```text
Time → O(N²)
Space → O(N)
```

The stack gives a cleaner linear solution.

---

# Complexity

Each asteroid is:

```text
pushed → at most once
popped → at most once
```

Therefore the total number of stack operations is O(N).

```text
Time  → O(N)
Space → O(N)
```

---

# Takeaway

Don't compare every pair.

Process asteroids from left → right and keep only
the surviving asteroids in a stack.

The key condition is:

```text
stack[-1] > 0 and asteroid < 0
```

Then repeatedly resolve the collision:

```text
smaller → pop
equal   → pop + destroy current
larger  → destroy current
```

### Mental Model

```text
positive → →
negative ← ←

Only:

    +  ←  collision
    ↑
   stack top
```

So:

```text
Asteroid Collision
        ↓
   Stack Simulation
        ↓
Check only + vs -
        ↓
Compare absolute sizes
        ↓
Pop destroyed asteroids
        ↓
Keep survivors
```
