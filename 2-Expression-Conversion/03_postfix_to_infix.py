"""
Problem:
Convert a Postfix expression to Infix.

Example:
    Postfix : AB+CD-*
    Infix   : ((A+B)*(C-D))

Pattern:
Stack + Left-to-Right Traversal

Key Observation:
In Postfix notation, the operator comes after its operands.

So we scan from left → right.

- Operand → push into stack
- Operator → pop two expressions,
               combine them as:
               (t2 operator t1)
               then push the result back

Why t2 first?
Because the first pop is the RIGHT operand.

Approach:
1. Traverse the Postfix expression from left → right.
2. If operand → push it into stack.
3. If operator:
       t1 = pop()   # right operand
       t2 = pop()   # left operand

       expression = "(" + t2 + operator + t1 + ")"

       push expression
4. The final stack element is the complete Infix expression.

Dry Run:
Postfix:
    AB+CD-*

Left → Right:

A → [A]
B → [A, B]
+ → [(A+B)]

C → [(A+B), C]
D → [(A+B), C, D]
- → [(A+B), (C-D)]

* → [((A+B)*(C-D))]

Result:
    ((A+B)*(C-D))

Complexity:
Time  → O(N)
Space → O(N)

Takeaway:
Postfix → Infix:
Scan left → right.
Operands are pushed.
For an operator:
pop right → pop left → combine → push back.
"""


def is_operand(char):
    """Check whether char is an operand."""
    return char.isalnum()


def postfix_to_infix(expression):
    stack = []

    # Postfix is processed from left → right.
    for char in expression:

        # Operand → push directly
        if is_operand(char):
            stack.append(char)

        # Operator → combine top two expressions
        else:
            t1 = stack.pop()  # Right operand
            t2 = stack.pop()  # Left operand

            combined = "(" + t2 + char + t1 + ")"

            stack.append(combined)

    return stack[-1]


# Example
expression = "AB+CD-*"

print(postfix_to_infix(expression))
# Output: ((A+B)*(C-D))