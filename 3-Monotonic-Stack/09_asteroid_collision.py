"""
Problem:
Given asteroids moving in a line:

    + → moving right
    - → moving left

When two asteroids collide:
- smaller one is destroyed
- equal sizes destroy both
- larger one survives

Pattern:
Stack + Simulation

Key Observation:
A collision happens only when:

    stack[-1] > 0 and asteroid < 0

because only a right-moving asteroid and a left-moving
asteroid can move toward each other.

Pseudocode:

    stack = []

    for asteroid in arr:

        alive = True

        while alive and asteroid < 0
              and stack and stack[-1] > 0:

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


Dry Run:
arr = [4, 7, 1, 1, 2, -3, -7, 17, 15, -16]

-3 destroys 2, 1, 1 and is then destroyed by 7.
-7 destroys 7 because their sizes are equal.
15 is destroyed by -16.
-16 is then destroyed by 17.

Final:
[4, 17]

Complexity:
Time  → O(N)
Space → O(N)

Takeaway:
Use a stack to keep only surviving asteroids.

Only + vs - can collide.
"""

def asteroid_collision(arr):
    stack = []

    for asteroid in arr:
        alive = True

        # Collision is possible only:
        # stack top moves right, current moves left.
        while (
            alive
            and asteroid < 0
            and stack
            and stack[-1] > 0
        ):
            top = stack[-1]

            # Current asteroid is larger.
            if top < abs(asteroid):
                stack.pop()

            # Both asteroids are destroyed.
            elif top == abs(asteroid):
                stack.pop()
                alive = False

            # Current asteroid is destroyed.
            else:
                alive = False

        if alive:
            stack.append(asteroid)

    return stack


# Example
arr = [4, 7, 1, 1, 2, -3, -7, 17, 15, -16]

print(asteroid_collision(arr))
# [4, 17]
