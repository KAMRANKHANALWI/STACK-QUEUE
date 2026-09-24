"""
Problem:
Check whether a string containing brackets is balanced.

The string may contain:
    ()
    {}
    []

A string is balanced if:
1. Every opening bracket has a corresponding closing bracket.
2. Every closing bracket has a corresponding opening bracket.
3. Brackets close in the correct order.


Pattern:
Balanced Parentheses → Stack

Key Observation:
Whenever we encounter a closing bracket, we need to
check the LAST opening bracket encountered.

"Last opening encountered" → LIFO → Stack.

So:

    Opening bracket → push into stack
    Closing bracket → match with stack top and pop


Approach:
1. Create an empty stack.
2. Traverse the string.
3. If the character is an opening bracket:
       push it into the stack.
4. If it is a closing bracket:
       - If stack is empty → no matching opening → False
       - Get stack top.
       - Pop it.
       - Check whether it matches the current closing bracket.
       - If not → False
5. At the end:
       Stack empty → True
       Stack not empty → False


Pseudocode:

is_balanced(s):

    stack = []

    for ch in s:

        if ch == '(' or ch == '{' or ch == '[':
            stack.push(ch)

        else:
            if stack is empty:
                return False

            top = stack.top()
            stack.pop()

            if ch == ')' and top != '(':
                return False

            elif ch == '}' and top != '{':
                return False

            elif ch == ']' and top != '[':
                return False

    return stack is empty


Matching:

    ')' → '('
    '}' → '{'
    ']' → '['


Dry Run 1:

s = "({[]})"

'(' → push
stack = ['(']

'{' → push
stack = ['(', '{']

'[' → push
stack = ['(', '{', '[']

']' → top = '[' → match → pop
stack = ['(', '{']

'}' → top = '{' → match → pop
stack = ['(']

')' → top = '(' → match → pop
stack = []

Stack is empty → True


Dry Run 2:

s = "({[})"

'(' → push
'{' → push
'[' → push

')' → top = '['

'[' does NOT match ')'

→ False


Important Cases:

1. Closing bracket with empty stack:

    s = ")"

No opening bracket exists.

→ False


2. Extra opening bracket:

    s = "(()"

After processing:

stack = ['(']

Stack is not empty.

→ False


3. Correct nesting:

    s = "({[]})"

→ True


Complexity:
Time  → O(N)
Space → O(N)

Why O(N) space?
In the worst case, the string contains only opening
brackets, so all N brackets are stored in the stack.

Takeaway:
Balanced Parentheses = Stack.

Opening → Push
Closing → Match with top + Pop

The key idea is:
Every closing bracket must match the
LAST opening bracket encountered.
"""


def is_balanced(s):
    stack = []

    for ch in s:

        # Opening bracket → push into stack
        if ch == "(" or ch == "{" or ch == "[":
            stack.append(ch)

        else:
            # Closing bracket with no opening bracket
            if not stack:
                return False

            top = stack.pop()

            # Check matching pair
            if ch == ")" and top != "(":
                return False

            elif ch == "}" and top != "{":
                return False

            elif ch == "]" and top != "[":
                return False

    # Stack must be empty after all matches
    return len(stack) == 0


# def is_balanced(s):
#     stack = []

#     opening = {"(", "{", "["}

#     matching = {
#         ")": "(",
#         "}": "{",
#         "]": "["
#     }

#     for ch in s:

#         # Opening bracket → store it
#         if ch in opening:
#             stack.append(ch)

#         # Closing bracket → match with latest opening
#         else:
#             if not stack:
#                 return False

#             top = stack.pop()

#             if top != matching[ch]:
#                 return False

#     # All opening brackets must have been matched
#     return len(stack) == 0


# Example
s = "({[]})"

print(is_balanced(s))  # True
