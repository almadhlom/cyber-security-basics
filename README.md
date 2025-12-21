# cyber-security-basics

A simple repository demonstrating basic cybersecurity concepts using Python.

---

## Python Tip: Use `enumerate()` in loops

When you need both the index and the value while looping over a list, using `enumerate()` is cleaner and more Pythonic.

### ❌ Not recommended

```python
passwords = ["admin123", "securePass!", "test123"]
for i in range(len(passwords)):
    print(i, passwords[i])
```

### ✅ Recommended

```python
passwords = ["admin123", "securePass!", "test123"]
for index, password in enumerate(passwords):
    print(index, password)
```

### Why use `enumerate()`?

- Improves readability
- Reduces indexing mistakes
- Follows Python best practices

---