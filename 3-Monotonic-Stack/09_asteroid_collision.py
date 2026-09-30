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

        while stack and stack[-1] > 0 and asteroid < 0
              and stack[-1] < abs(asteroid):

            stack.pop()

        if stack and stack[-1] > 0 and asteroid < 0:

            if stack[-1] == abs(asteroid):
                stack.pop()

            # else:
            # stack[-1] is larger → current asteroid dies

        else:
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

        # Remove smaller right-moving asteroids.
        while stack and stack[-1] > 0 and asteroid < 0 and stack[-1] < abs(asteroid):
            stack.pop()

        # Collision is still possible after removing smaller asteroids.
        if stack and stack[-1] > 0 and asteroid < 0:

            # Equal sizes → both destroyed.
            if stack[-1] == abs(asteroid):
                stack.pop()

            # Stack top is larger → current asteroid is destroyed.
            # Nothing to do.

        else:
            # No collision → current asteroid survives.
            stack.append(asteroid)

    return stack


# Example
arr = [4, 7, 1, 1, 2, -3, -7, 17, 15, -16]

print(asteroid_collision(arr))
# [4, 17]
