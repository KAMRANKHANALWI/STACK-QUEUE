"""
Problem:
Convert a Prefix expression to Postfix.

Example:
    Prefix  : *+AB-CD
    Postfix : AB+CD-*

Pattern:
Stack + Right-to-Left Traversal

Key Observation:
Prefix places the operator before its operands.

So we scan from right → left.

- Operand → push into stack
- Operator → pop two expressions,
               combine them as:
               t1 + t2 + operator
               then push the result back

Approach:
1. Traverse the Prefix expression from right → left.
2. If operand → push it into stack.
3. If operator:
       t1 = pop()
       t2 = pop()

       expression = t1 + t2 + operator

       push expression
4. The final stack element is the Postfix expression.

Dry Run:
Prefix:
    *+AB-CD

Right → Left:

D → [D]
C → [D, C]
- → [CD-]

B → [CD-, B]
A → [CD-, B, A]
+ → [CD-, AB+]

* → [AB+CD-*]

Result:
    AB+CD-*

Complexity:
Time  → O(N)
Space → O(N)

Takeaway:
Prefix → Postfix:
Scan right → left.
Operands are pushed.
For an operator:
pop two → combine as t1 + t2 + operator → push back.
"""


def is_operand(char):
    """Check whether char is an operand."""
    return char.isalnum()


def prefix_to_postfix(expression):
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

            combined = t1 + t2 + char

            stack.append(combined)

    return stack[-1]


# Example
expression = "*+AB-CD"

print(prefix_to_postfix(expression))
# Output: AB+CD-*