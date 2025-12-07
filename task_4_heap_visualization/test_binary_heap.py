"""
Юніт-тести для бінарної купи у завданні 4.

Перевіряє структуру купи та побудову дерева.
"""

import pytest
import sys
from pathlib import Path

# Додаємо корінь проекту до шляху для абсолютних імпортів
project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

# Додаємо директорію завдання до шляху (важливо: першою, щоб уникнути конфлікту з task_3)
task_dir = Path(__file__).parent
if str(task_dir) not in sys.path:
    sys.path.insert(0, str(task_dir))

# Спочатку пробуємо абсолютний імпорт, потім відносний
try:
    from task_4_heap_visualization.binary_heap import BinaryHeap, Node
except ImportError:
    from binary_heap import BinaryHeap, Node


@pytest.mark.unit
class TestBinaryHeap:
    """Тести для класу BinaryHeap."""
    
    def test_create_empty_heap(self):
        """Тест створення порожньої купи."""
        heap = BinaryHeap()
        assert len(heap.heap) == 0
        assert heap.root is None
    
    def test_insert_single_element(self):
        """Тест вставки одного елемента."""
        heap = BinaryHeap()
        heap.insert(5)
        assert len(heap.heap) == 1
        assert heap.heap[0] == 5
    
    def test_insert_multiple_elements(self):
        """Тест вставки кількох елементів."""
        heap = BinaryHeap()
        heap.insert(3)
        heap.insert(1)
        heap.insert(4)
        heap.insert(2)
        assert len(heap.heap) == 4
    
    def test_build_tree_from_empty_heap(self):
        """Тест побудови дерева з порожньої купи."""
        heap = BinaryHeap()
        root = heap.build_tree_from_heap()
        assert root is None
    
    def test_build_tree_from_single_element(self):
        """Тест побудови дерева з одного елемента."""
        heap = BinaryHeap()
        heap.insert(5)
        root = heap.build_tree_from_heap()
        assert root is not None
        assert root.val == 5
        assert root.left is None
        assert root.right is None
    
    def test_build_tree_from_multiple_elements(self):
        """Тест побудови дерева з кількох елементів."""
        heap = BinaryHeap()
        heap.insert(0)
        heap.insert(4)
        heap.insert(1)
        heap.insert(5)
        heap.insert(10)
        heap.insert(3)
        
        root = heap.build_tree_from_heap()
        assert root is not None
        assert root.val == 0  # Корінь купи
    
    def test_heap_property_maintained(self):
        """Тест, що властивість купи зберігається."""
        heap = BinaryHeap()
        heap.insert(5)
        heap.insert(3)
        heap.insert(1)
        heap.insert(4)
        heap.insert(2)
        
        # Перевіряємо, що батьківський вузол менший за дочірні
        root = heap.build_tree_from_heap()
        if root and root.left:
            assert root.val <= root.left.val
        if root and root.right:
            assert root.val <= root.right.val
    
    def test_is_empty_on_empty_heap(self):
        """Тест is_empty() на порожній купі."""
        heap = BinaryHeap()
        assert heap.is_empty() is True
    
    def test_is_empty_on_non_empty_heap(self):
        """Тест is_empty() на непорожній купі."""
        heap = BinaryHeap()
        heap.insert(5)
        assert heap.is_empty() is False
    
    def test_peek_on_empty_heap(self):
        """Тест peek() на порожній купі."""
        heap = BinaryHeap()
        assert heap.peek() is None
    
    def test_peek_on_single_element(self):
        """Тест peek() на купі з одним елементом."""
        heap = BinaryHeap()
        heap.insert(5)
        assert heap.peek() == 5
        assert len(heap.heap) == 1  # Елемент не видалено
    
    def test_peek_on_multiple_elements(self):
        """Тест peek() на купі з кількома елементами."""
        heap = BinaryHeap()
        heap.insert(5)
        heap.insert(3)
        heap.insert(1)
        heap.insert(4)
        
        # peek() повинен повернути мінімальний елемент
        assert heap.peek() == 1
        # Елемент не повинен бути видалено
        assert len(heap.heap) == 4
        assert heap.heap[0] == 1
    
    def test_peek_does_not_modify_heap(self):
        """Тест, що peek() не змінює купу."""
        heap = BinaryHeap()
        heap.insert(5)
        heap.insert(3)
        heap.insert(1)
        
        initial_size = len(heap.heap)
        initial_min = heap.heap[0]
        
        # Викликаємо peek() кілька разів
        assert heap.peek() == initial_min
        assert heap.peek() == initial_min
        assert heap.peek() == initial_min
        
        # Купа не повинна змінитися
        assert len(heap.heap) == initial_size
        assert heap.heap[0] == initial_min
    
    def test_extract_min_on_empty_heap(self):
        """Тест extract_min() на порожній купі."""
        heap = BinaryHeap()
        assert heap.extract_min() is None
        assert heap.is_empty() is True
    
    def test_extract_min_on_single_element(self):
        """Тест extract_min() на купі з одним елементом."""
        heap = BinaryHeap()
        heap.insert(5)
        
        min_val = heap.extract_min()
        assert min_val == 5
        assert heap.is_empty() is True
        assert len(heap.heap) == 0
    
    def test_extract_min_on_multiple_elements(self):
        """Тест extract_min() на купі з кількома елементами."""
        heap = BinaryHeap()
        heap.insert(5)
        heap.insert(3)
        heap.insert(1)
        heap.insert(4)
        heap.insert(2)
        
        # Перший мінімальний елемент
        min_val = heap.extract_min()
        assert min_val == 1
        assert len(heap.heap) == 4
        # Після видалення новий мінімум повинен бути наступним найменшим
        assert heap.peek() <= 5  # Може бути 2, 3, 4 або 5
    
    def test_extract_min_maintains_heap_property(self):
        """Тест, що extract_min() зберігає властивість купи."""
        heap = BinaryHeap()
        values = [5, 3, 1, 4, 2, 6, 0]
        for val in values:
            heap.insert(val)
        
        # Вилучаємо мінімальні елементи послідовно
        extracted = []
        while not heap.is_empty():
            min_val = heap.extract_min()
            extracted.append(min_val)
            # Перевіряємо, що властивість купи зберігається
            if not heap.is_empty():
                root = heap.build_tree_from_heap()
                if root and root.left:
                    assert root.val <= root.left.val
                if root and root.right:
                    assert root.val <= root.right.val
        
        # Перевіряємо, що елементи вилучені в порядку зростання
        assert extracted == sorted(values)
    
    def test_extract_min_sequence(self):
        """Тест послідовного вилучення мінімальних елементів."""
        heap = BinaryHeap()
        heap.insert(10)
        heap.insert(5)
        heap.insert(15)
        heap.insert(3)
        heap.insert(7)
        
        # Вилучаємо всі елементи
        extracted = []
        while not heap.is_empty():
            extracted.append(heap.extract_min())
        
        # Елементи повинні бути вилучені в порядку зростання
        assert extracted == [3, 5, 7, 10, 15]
        assert heap.is_empty() is True
    
    def test_peek_after_extract_min(self):
        """Тест peek() після extract_min()."""
        heap = BinaryHeap()
        heap.insert(5)
        heap.insert(3)
        heap.insert(1)
        
        assert heap.peek() == 1
        heap.extract_min()
        assert heap.peek() != 1  # Мінімум змінився
        assert heap.peek() in [3, 5]  # Новий мінімум

