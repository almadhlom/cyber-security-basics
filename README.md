# Cyber Security Basics

A collection of basic cyber security tools and educational resources.

## Tools

- `password-checker.py` - Simple password strength checker

## Python Tips

### Tip #147: Use enumerate() for index+value in loops

Instead of:
```python
for i in range(len(items)):
    print(i, items[i])
```

Use enumerate():
```python
for i, item in enumerate(items):
    print(i, item)
```

This is more Pythonic and readable!
