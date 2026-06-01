# Daily-Info Python Tip: Use `enumerate()` for index+value in loops

When looping through a list in Python, you often need both the index and the value. Instead of manually tracking an index variable, use the built-in `enumerate()` function.

## How it works

`enumerate()` returns pairs of (index, value) for each item in an iterable:

```python
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: cherry
```

## Custom start index

You can specify a starting number with the `start` parameter:

```python
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
# Output:
# 1. apple
# 2. banana
# 3. cherry
```

## Why use it?

- **Cleaner code** — no need to manually increment a counter
- **Less error-prone** — avoids off-by-one mistakes
- **More Pythonic** — follows the language's best practices

Start using `enumerate()` today to make your loops simpler and more readable!