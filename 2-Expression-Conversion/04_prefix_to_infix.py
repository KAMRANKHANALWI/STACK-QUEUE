"""
Problem:
Convert a Prefix expression to Infix.

Example:
    Prefix : *+AB-CD
    Infix  : ((A+B)*(C-D))

Pattern:
Stack + Right-to-Left Traversal

Key Observation:
In Prefix notation, the operator comes before its operands.

So we scan from right → left.

- Operand → push into stack
- Operator → pop two operands/expressions,
               combine them with the operator,
               then push the result back

Approach:
1. Traverse the expression from right → left.
2. If operand → push it into stack.
3. If operator:
       t1 = pop()
       t2 = pop()

       expression = "(" + t1 + operator + t2 + ")"

       push expression
4. The final stack element is the complete Infix expression.

Dry Run:
Prefix:
    *+AB-CD

Right → Left:

D → [D]
C → [D, C]
- → [(C-D)]

B → [(C-D), B]
A → [(C-D), B, A]
+ → [(C-D), (A+B)]

* → [((A+B)*(C-D))]

Result:
    ((A+B)*(C-D))

Complexity:
Time  → O(N)
Space → O(N)

Takeaway:
Prefix → Infix:
Scan right → left.
Operands are pushed.
For an operator, pop two expressions,
combine them as (left operator right),
then push the result back.
"""


def is_operand(char):
    """Check whether char is an operand."""
    return char.isalnum()


def prefix_to_infix(expression):
    stack = []

    # Prefix is processed from right → left.
    for char in reversed(expression):

        # Operand → push directly
        if is_operand(char):
            stack.append(char)

        # Operator → combine top two expressions
        else:
            t1 = stack.pop()
            t2 = stack.pop()

            combined = "(" + t1 + char + t2 + ")"

            stack.append(combined)

    return stack[-1]


# Example
expression = "*+AB-CD"

print(prefix_to_infix(expression))
# Output: ((A+B)*(C-D))