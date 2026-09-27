"""
Problem:
Convert an Infix expression to Postfix.

Example:
    Infix  : a + b * (c ^ d - e)
    Postfix: abcd^e-*+

Pattern:
Stack + Operator Precedence

Key Observation:
Operands go directly to the answer.

Operators cannot always go directly to the answer because
their order depends on:
- precedence
- associativity
- parentheses

So:
- Operand  → add to answer
- '('      → push to stack
- ')'      → pop until '('
- Operator → pop higher/equal priority operators, then push

Precedence:
    ^       → 3
    * /     → 2
    + -     → 1

Search / Processing:
Scan the infix expression from left → right.

Approach:
1. If operand → add to answer.
2. If '(' → push into stack.
3. If ')' → pop until '(' is found, then remove '('.
4. If operator:
   - Pop operators with higher precedence.
   - For left-associative operators, also pop equal precedence.
   - Push current operator.
5. After traversal, pop remaining operators.

Dry Run:
Expression:
    a + b * (c ^ d - e)

Postfix:
    a b c d ^ e - * +

    → abcd^e-*+

Complexity:
Time  → O(N)
Space → O(N)

Takeaway:
Infix → Postfix = operands go to answer,
operators wait in a stack according to precedence.
"""


def precedence(operator):
    """Return precedence of an operator."""
    if operator == "^":
        return 3

    if operator in "*/":
        return 2

    if operator in "+-":
        return 1

    return -1


def is_operand(char):
    """Check whether char is an operand."""
    return char.isalnum()


def infix_to_postfix(expression):
    stack = []
    answer = []

    for char in expression:

        # 1. Operand → directly to answer
        if is_operand(char):
            answer.append(char)

        # 2. Opening bracket → push
        elif char == "(":
            stack.append(char)

        # 3. Closing bracket → pop until '('
        elif char == ")":
            while stack and stack[-1] != "(":
                answer.append(stack.pop())

            # Remove '('
            if stack:
                stack.pop()

        # 4. Operator
        else:
            while (
                stack
                and stack[-1] != "("
                and (
                    precedence(char) < precedence(stack[-1])
                    or (
                        precedence(char) == precedence(stack[-1])
                        and char != "^"
                    )
                )
            ):
                answer.append(stack.pop())

            stack.append(char)

    # 5. Pop remaining operators
    while stack:
        answer.append(stack.pop())

    return "".join(answer)


# Example
expression = "a+b*(c^d-e)"

print(infix_to_postfix(expression))
# Output: abcd^e-*+