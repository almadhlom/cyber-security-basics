# Daily Python Tips and Information

## Tip #159: Use enumerate() for Index+Value in Loops

When you need both the index and value while iterating over a list, use Python's built-in `enumerate()` function instead of managing indices manually.

### ❌ Without enumerate()
```python
items = ['apple', 'banana', 'cherry']

# Manual index management
for i in range(len(items)):
    print(f"Index: {i}, Item: {items[i]}")
```

### ✅ With enumerate()
```python
items = ['apple', 'banana', 'cherry']

# Clean and Pythonic
for index, item in enumerate(items):
    print(f"Index: {index}, Item: {item}")
```

### Custom Starting Index
You can also specify a starting index:
```python
items = ['apple', 'banana', 'cherry']

# Start counting from 1 instead of 0
for index, item in enumerate(items, start=1):
    print(f"Position: {index}, Item: {item}")
```

### Benefits
- ✅ More readable and Pythonic
- ✅ Fewer potential off-by-one errors
- ✅ Better performance (no need to call `len()` and index into list)
- ✅ Works with any iterable (lists, tuples, strings, etc.)

### Real-World Example (Cyber Security Context)
```python
passwords = ['password123', 'secure_pass456', 'weak_pass']

for position, password in enumerate(passwords, start=1):
    strength = check_password_strength(password)
    print(f"Password {position}: {strength}")
```

---

**Tip of the Day:** Master `enumerate()` to write cleaner, more efficient Python code!
