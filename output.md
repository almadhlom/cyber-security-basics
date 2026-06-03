# Daily-Info Python Tip: `enumerate()`

**让循环同时获取索引和值**

## 引言

在Python中遍历列表时，经常需要同时获取元素的索引和值。初学者可能会这样写：

```python
fruits = ['apple', 'banana', 'cherry']
for i in range(len(fruits)):
    print(i, fruits[i])
```

但Python提供了一个更优雅的内置函数——`enumerate()`，它能简化这一过程。

## 基本用法

`enumerate()`接收一个可迭代对象，返回一个枚举对象，每次迭代产生一个包含索引和值的元组：

```python
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)
```

输出：
```
0 apple
1 banana
2 cherry
```

## 自定义起始索引

`enumerate()`的第二个参数允许指定起始索引（默认为0）：

```python
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
```

输出：
```
1. apple
2. banana
3. cherry
```

## 总结

| 场景 | 传统写法 | enumerate写法 |
|------|----------|---------------|
| 基本遍历 | `range(len(list))` | `enumerate(list)` |
| 自定义起始值 | `range(1, len(list)+1)` | `enumerate(list, start=1)` |

`enumerate()`让代码更简洁、可读性更强，是Pythonic编程的典型体现。养成使用它的习惯，能让你的循环代码更加清晰高效。