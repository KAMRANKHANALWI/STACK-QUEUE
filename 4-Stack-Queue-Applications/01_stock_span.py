
"""
Problem:
Given daily stock prices, find the stock span for each day.

Stock Span:
Number of consecutive previous days (including today)
where the price was less than or equal to today's price.

Example:
prices = [7, 2, 1, 3, 3, 1, 8]

Output:
[1, 1, 1, 3, 4, 1, 7]


Pattern:
Previous Greater Element + Monotonic Stack.

Key Observation:
For every day, find the nearest previous price
that is STRICTLY GREATER than the current price.

The span is the distance between their indices.

If no greater price exists:
    span = current_index + 1


Brute Force:
For every day, traverse backwards and count
consecutive prices <= current price.

Complexity:
Time  -> O(N²)
Space -> O(N) for the answer.


Optimal:
Maintain a decreasing stack of (price, index).

For every current price:

    1. Pop while stack.top.price <= current price.
    2. If stack is empty:
           span = i + 1
       Otherwise:
           span = i - stack.top.index
    3. Push (current_price, i).


Why <= ?

Equal prices are also included in the stock span.

Complexity:
Time  -> O(N) amortized
Space -> O(N)

Takeaway:
Stock Span = Previous Greater Element.

The stack stores only useful previous greater candidates.
Each element is pushed and popped at most once.
"""


# --------------------------------------------------
# Brute Force
# --------------------------------------------------

def stock_span_brute(prices):
    n = len(prices)
    answer = []

    for i in range(n):
        span = 1

        j = i - 1

        while j >= 0 and prices[j] <= prices[i]:
            span += 1
            j -= 1

        answer.append(span)

    return answer


# --------------------------------------------------
# Optimal — Monotonic Stack
# --------------------------------------------------

def stock_span_optimal(prices):
    stack = []  # (price, index)
    answer = []

    for i in range(len(prices)):

        # Remove previous prices <= current price
        while stack and stack[-1][0] <= prices[i]:
            stack.pop()

        # Find distance from previous greater price
        if not stack:
            span = i + 1
        else:
            span = i - stack[-1][1]

        answer.append(span)

        # Store current price and index
        stack.append((prices[i], i))

    return answer


# --------------------------------------------------
# Online Stock Span — Class Implementation
# --------------------------------------------------

class StockSpanner:

    def __init__(self):
        self.stack = []
        self.index = -1

    def next(self, price):

        self.index += 1

        # Remove previous prices <= current price
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()

        # Calculate current stock span
        if not self.stack:
            span = self.index + 1
        else:
            span = self.index - self.stack[-1][1]

        self.stack.append((price, self.index))

        return span


# --------------------------------------------------
# Example
# --------------------------------------------------

prices = [7, 2, 1, 3, 3, 1, 8]

print("Brute:  ", stock_span_brute(prices))
print("Optimal:", stock_span_optimal(prices))

# Online implementation
spanner = StockSpanner()

result = [spanner.next(price) for price in prices]

print("Online: ", result)

# spanner = StockSpanner()

# print(spanner.next(7))  # 1
# print(spanner.next(2))  # 1
# print(spanner.next(1))  # 1
# print(spanner.next(3))  # 3
# print(spanner.next(3))  # 4
# print(spanner.next(1))  # 1
print(spanner.next(8))  # 7