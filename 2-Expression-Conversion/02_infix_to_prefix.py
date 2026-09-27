"""
Problem:
Convert an Infix expression to Prefix.

Example:
    Infix  : a + b * (c ^ d - e)
    Prefix : +a*-^cde b
             +a*b-c^de

Pattern:
Reverse + Swap Brackets + Infix → Postfix + Reverse

Key Observation:
Prefix is difficult to build directly.

So:
    1. Reverse the infix expression
    2. Swap '(' and ')'
    3. Convert it to postfix
    4. Reverse the postfix result

Important:
Because the expression is reversed, the associativity
condition for '^' changes during the postfix conversion.

Precedence:
    ^       → 3
    * /     → 2
    + -     → 1

Approach:
1. Reverse the expression.
2. Swap:
       '(' → ')'
       ')' → '('
3. Convert the modified expression to postfix.
4. Reverse the postfix result.

Dry Run:
Expression:
    a+b*(c^d-e)

Reverse:
    )e-d^c(*b+a(

Swap brackets:
    (e-d^c)*b+a

Postfix:
    edc^-b*a+

Reverse:
    +a*b-^cde

Complexity:
Time  → O(N)
Space → O(N)

Takeaway:
Infix → Prefix:
Reverse → Swap brackets → Postfix → Reverse.
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


def infix_to_prefix(expression):
    # Step 1 + 2:
    # Reverse expression and swap brackets.
    expression = expression[::-1]

    expression = expression.translate(
        str.maketrans("()", ")(")
    )

    stack = []
    postfix = []

    for char in expression:

        # Operand → directly to answer
        if is_operand(char):
            postfix.append(char)

        # Opening bracket → push
        elif char == "(":
            stack.append(char)

        # Closing bracket → pop until '('
        elif char == ")":
            while stack and stack[-1] != "(":
                postfix.append(stack.pop())

            if stack:
                stack.pop()

        # Operator
        else:
            while (
                stack
                and stack[-1] != "("
                and (
                    precedence(char) < precedence(stack[-1])
                    or (
                        precedence(char) == precedence(stack[-1])
                        and char == "^"
                    )
                )
            ):
                postfix.append(stack.pop())

            stack.append(char)

    # Pop remaining operators
    while stack:
        postfix.append(stack.pop())

    # Step 4:
    # Reverse postfix to obtain prefix.
    return "".join(postfix[::-1])


# Example
expression = "a+b*(c^d-e)"

print(infix_to_prefix(expression))
# Output: +a*b-^cde