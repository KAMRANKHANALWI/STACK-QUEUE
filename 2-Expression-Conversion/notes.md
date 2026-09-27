# Expression Conversion

## Expression Types

### Infix

Operator between operands.

```text
A + B
```

### Prefix

Operator before operands.

```text
+ A B
```

### Postfix

Operator after operands.

```text
A B +
```

---

## Why Stack?

Operators cannot always be placed directly into the answer.

They may need to wait because of:

- operator precedence
- associativity
- parentheses

```text
Expression
    ↓
Operands  → output
Operators → stack
```

---

## Operator Precedence

```text
^        → 3

* /      → 2

+ -      → 1
```

Higher precedence operators are processed first.

---

## Associativity

```text
^        → Right associative

* /      → Left associative

+ -      → Left associative
```

Important:

```text
^ → right associative
```

This matters especially when converting Infix ↔ Prefix.

---

## Core Pattern

### Infix → Postfix

```text
Scan: Left → Right

Operand
    → output

'('
    → push

')'
    → pop until '('

Operator
    → pop higher/equal priority operators
    → push current operator

End
    → pop remaining operators
```

---

### Infix → Prefix

```text
Reverse expression
        ↓
Swap '(' and ')'
        ↓
Convert to Postfix
        ↓
Reverse result
        ↓
Prefix
```

---

### Postfix → Infix

```text
Scan: Left → Right

Operand
    → push

Operator
    → pop right
    → pop left
    → (left operator right)
    → push
```

---

### Prefix → Infix

```text
Scan: Right → Left

Operand
    → push

Operator
    → pop first
    → pop second
    → (first operator second)
    → push
```

---

### Postfix → Prefix

```text
Scan: Left → Right

Operand
    → push

Operator
    → pop right
    → pop left
    → operator + left + right
    → push
```

---

### Prefix → Postfix

```text
Scan: Right → Left

Operand
    → push

Operator
    → pop first
    → pop second
    → first + second + operator
    → push
```

---

## Problems

1. Infix → Postfix
2. Infix → Prefix
3. Postfix → Infix
4. Prefix → Infix
5. Postfix → Prefix
6. Prefix → Postfix

---

## Conversion Cheat Sheet

| Conversion | Traversal | Operator Combination |
|---|---|---|
| Infix → Postfix | Left → Right | Precedence + stack |
| Infix → Prefix | Reverse → Postfix → Reverse | Precedence + stack |
| Postfix → Infix | Left → Right | `(left op right)` |
| Prefix → Infix | Right → Left | `(left op right)` |
| Postfix → Prefix | Left → Right | `op + left + right` |
| Prefix → Postfix | Right → Left | `left + right + op` |

---

## Key Pattern

```text
Expression Conversion
        ↓
      Stack
        +
Precedence / Associativity
        +
    Traversal
```

The main thing to remember is:

```text
Postfix → scan Left → Right

Prefix → scan Right → Left
```

For conversion into another notation:

```text
Operator position changes.

Postfix:
    left right operator

Prefix:
    operator left right

Infix:
    left operator right
```

---

## Key Takeaway

Expression conversion is mainly about understanding:

```text
1. Stack
2. Operator precedence
3. Associativity
4. Traversal direction
5. Operand/operator combination
6. Parentheses
```

Once these rules are clear, all six conversions become variations of the same stack pattern.
