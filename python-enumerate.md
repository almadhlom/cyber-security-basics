# Python Tip: Using enumerate()

## 📌 What is enumerate()?
The `enumerate()` function in Python allows you to loop through a list and get both the index and the value at the same time.

---

## ❌ Without enumerate
```python
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(i, fruits[i])
```

---

## ✅ With enumerate (Better Way)
```python
fruits = ["apple", "banana", "cherry"]
for index, value in enumerate(fruits):
    print(index, value)
```

### Output
```
0 apple
1 banana
2 cherry
```

## 💡 Why use enumerate?
- Cleaner and more readable code
- No need to use range() and len()
- Reduces chances of errors