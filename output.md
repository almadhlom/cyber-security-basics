### Daily-Info Python Tip: Use `enumerate()` for index+value in loops

When looping over a list in Python, beginners often use `range(len(list))` to access both index and value. A cleaner, more Pythonic way is to use `enumerate()`.

**Before (clunky):**
```python
fruits = ['apple', 'banana', 'cherry']
for i in range(len(fruits)):
    print(i, fruits[i])
```

**After (elegant):**
```python
fruits = ['apple', 'banana', 'cherry']
for i, fruit in enumerate(fruits):
    print(i, fruit)
```

Both produce:
```
0 apple
1 banana
2 cherry
```

`enumerate()` returns a tuple of `(index, value)` for each item. You can also start the index at a different number by passing a `start` parameter:
```python
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
```
Output:
```
1. apple
2. banana
3. cherry
```

**Key benefit:** Cleaner code, no need for manual indexing, and it works with any iterable (lists, tuples, strings, etc.).