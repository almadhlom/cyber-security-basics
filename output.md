# Daily-Info: Python Tip - Use `enumerate()` for index+value in loops

When iterating over a list or other sequence in Python, you often need both the index and the value. Instead of manually managing a counter variable, use the built-in `enumerate()` function.

**Basic Example:**
```python
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: cherry
```

**Common Use Cases:**
- **Modifying items by index**: Update specific elements in a list based on their position.
- **Creating numbered lists**: Generate output with sequential numbering.
- **Tracking iteration progress**: Display progress percentage in loops.

**Pro Tip:** Use the optional `start` parameter to begin counting from a different number:
```python
for i, item in enumerate(items, start=1):
    print(f"Item {i}: {item}")
```

**Why use it?** `enumerate()` is more readable and Pythonic than manual counters, reduces boilerplate code, and avoids off-by-one errors.