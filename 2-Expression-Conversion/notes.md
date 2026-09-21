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

Operators may need to wait until their operands or higher-priority operators are processed.

```text
Expression
    ↓
Operands → output
Operators → stack
```

---

## Operator Precedence

```text
^
*, /
+, -
```

Higher precedence operators are processed first.

---

## Associativity

```text
^       → Right associative
*, /    → Left associative
+, -    → Left associative
```

---

## Core Pattern

```text
Operand
    → output

Operator
    → compare precedence
    → stack

Opening '('
    → push

Closing ')'
    → pop until '('
```

---

## Problems

1. Infix → Postfix
2. Prefix → Infix
3. Prefix → Postfix
4. Postfix → Prefix
5. Postfix → Infix
6. Infix → Prefix

---

## Key Takeaway

Expression conversion is primarily:

```text
Stack
+
Operator precedence
+
Associativity
+
Parentheses
```

Once these rules are clear, the six conversions become variations of the same idea.
