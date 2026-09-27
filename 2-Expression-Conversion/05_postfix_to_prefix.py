"""
Problem:
Convert a Postfix expression to Prefix.

Example:
    Postfix : AB+CD-*
    Prefix  : *+AB-CD

Pattern:
Stack + Left-to-Right Traversal

Key Observation:
In Postfix notation, the operator comes after its operands.

So we scan from left → right.

- Operand → push into stack
- Operator → pop two expressions
- First pop  → right operand
- Second pop → left operand

Then build:

    operator + left + right

and push the result back.

Approach:
1. Traverse the Postfix expression from left → right.
2. If operand → push it into stack.
3. If operator:
       t1 = pop()   # right operand
       t2 = pop()   # left operand

       expression = operator + t2 + t1

       push expression
4. The final stack element is the Prefix expression.

Dry Run:
Postfix:
    AB+CD-*

A → [A]
B → [A, B]

+ → ["+AB"]

C → ["+AB", C]
D → ["+AB", C, D]

- → ["+AB", "-CD"]

* → ["*+AB-CD"]

Result:
    *+AB-CD

Complexity:
Time  → O(N)
Space → O(N)

Takeaway:
Postfix → Prefix:
Scan left → right.

For an operator:
pop right → pop left → combine as

    operator + left + right

then push back.
"""


def is_operand(char):
    """Check whether char is an operand."""
    return char.isalnum()


def postfix_to_prefix(expression):
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

            combined = char + t2 + t1

            stack.append(combined)

    return stack[-1]


# Example
expression = "AB+CD-*"

print(postfix_to_prefix(expression))
# Output: *+AB-CD