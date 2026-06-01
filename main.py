"""
Python Tip: Using enumerate() for Index + Value in Loops
=======================================================

enumerate() is a built-in function that adds a counter to an iterable,
returning pairs of (index, value) as you loop through it.

This is more Pythonic and efficient than manually tracking an index variable.
"""

from typing import List, Any, Iterable, Tuple
import unittest


def demonstrate_enumerate_basics() -> None:
    """Show basic usage of enumerate() with different iterables."""
    
    # Example 1: Basic list iteration
    fruits = ['apple', 'banana', 'cherry']
    print("Example 1: Basic list iteration")
    for index, fruit in enumerate(fruits):
        print(f"Index {index}: {fruit}")
    print()
    
    # Example 2: Starting from a custom index
    print("Example 2: Starting from index 1")
    for index, fruit in enumerate(fruits, start=1):
        print(f"Item {index}: {fruit}")
    print()
    
    # Example 3: With strings
    word = "Python"
    print("Example 3: Iterating over a string")
    for index, char in enumerate(word):
        print(f"Position {index}: '{char}'")
    print()


def find_items_with_index(items: List[Any], target: Any) -> List[Tuple[int, Any]]:
    """
    Find all occurrences of a target item in a list with their indices.
    
    Args:
        items: List to search through
        target: Item to find
        
    Returns:
        List of (index, value) tuples where value matches target
        
    Raises:
        TypeError: If items is not a list
    """
    if not isinstance(items, list):
        raise TypeError("items must be a list")
    
    # Using enumerate() to get both index and value
    return [(index, item) for index, item in enumerate(items) if item == target]


def process_list_with_indices(data: List[Any]) -> List[str]:
    """
    Process a list and create formatted strings with indices.
    
    Args:
        data: List of items to process
        
    Returns:
        List of formatted strings
        
    Raises:
        ValueError: If data is empty
    """
    if not data:
        raise ValueError("Input list cannot be empty")
    
    # enumerate() makes it easy to include indices in formatted output
    return [f"Position {idx}: {value}" for idx, value in enumerate(data)]


def update_list_with_indices(items: List[Any]) -> List[Any]:
    """
    Modify list items at specific indices using enumerate().
    
    This demonstrates how enumerate() allows you to modify items
    while iterating, which is cleaner than using range(len()).
    
    Args:
        items: List to modify
        
    Returns:
        Modified list with even-indexed items uppercased (if strings)
    """
    for index, item in enumerate(items):
        # Modify items at even indices
        if index % 2 == 0 and isinstance(item, str):
            items[index] = item.upper()
    return items


# Test cases
class TestEnumerateUsage(unittest.TestCase):
    """Test cases for enumerate() usage examples."""
    
    def test_find_items_with_index(self):
        """Test finding items with their indices."""
        items = ['a', 'b', 'a', 'c', 'a']
        result = find_items_with_index(items, 'a')
        self.assertEqual(result, [(0, 'a'), (2, 'a'), (4, 'a')])
        
        # Test with no matches
        result = find_items_with_index(items, 'z')
        self.assertEqual(result, [])
        
        # Test with invalid input
        with self.assertRaises(TypeError):
            find_items_with_index("not a list", 'a')
    
    def test_process_list_with_indices(self):
        """Test processing list with indices."""
        data = ['apple', 'banana', 'cherry']
        result = process_list_with_indices(data)
        expected = [
            "Position 0: apple",
            "Position 1: banana",
            "Position 2: cherry"
        ]
        self.assertEqual(result, expected)
        
        # Test with empty list
        with self.assertRaises(ValueError):
            process_list_with_indices([])
    
    def test_update_list_with_indices(self):
        """Test updating list items using enumerate()."""
        items = ['hello', 'world', 'python', 'code']
        result = update_list_with_indices(items)
        self.assertEqual(result, ['HELLO', 'world', 'PYTHON', 'code'])
        
        # Test with mixed types
        mixed = ['hello', 42, 'world', True]
        result = update_list_with_indices(mixed)
        self.assertEqual(result, ['HELLO', 42, 'WORLD', True])


def main():
    """Main function to demonstrate enumerate() usage."""
    
    print("=" * 50)
    print("Python Tip: Using enumerate() for Index + Value")
    print("=" * 50)
    print()
    
    # Demonstrate basic usage
    demonstrate_enumerate_basics()
    
    # Demonstrate practical applications
    print("Example 4: Finding items with indices")
    items = ['apple', 'banana', 'apple', 'cherry', 'apple']
    target = 'apple'
    found = find_items_with_index(items, target)
    print(f"Found '{target}' at positions: {[idx for idx, _ in found]}")
    print()
    
    print("Example 5: Processing list with formatted output")
    data = ['Python', 'Java', 'JavaScript', 'C++']
    processed = process_list_with_indices(data)
    for line in processed:
        print(line)
    print()
    
    print("Example 6: Modifying list items at specific indices")
    words = ['hello', 'world', 'python', 'code']
    print(f"Before: {words}")
    modified = update_list_with_indices(words)
    print(f"After:  {modified}")
    print()
    
    # Run tests
    print("Running tests...")
    unittest.main(argv=[''], verbosity=2, exit=False)


if __name__ == "__main__":
    main()