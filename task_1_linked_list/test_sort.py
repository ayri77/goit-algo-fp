"""
Юніт-тести для сортування однозв'язного списку.

Перевіряє методи класу sort() та sorted().
"""

import pytest
import sys
from pathlib import Path

# Додаємо директорію завдання до шляху
sys.path.insert(0, str(Path(__file__).parent))

from linked_list import LinkedList


@pytest.mark.unit
class TestSortMethod:
    """Тести для методу класу sort()."""
    
    def test_sort_empty_list(self):
        """Тест сортування порожнього списку."""
        ll = LinkedList()
        result = ll.sort()
        assert result is ll  # Повертає self
        assert result.head is None
    
    def test_sort_single_element(self):
        """Тест сортування списку з одним елементом."""
        ll = LinkedList()
        ll.append(5)
        result = ll.sort()
        
        assert result is ll
        assert result.head.data == 5
        assert result.head.next is None
    
    def test_sort_already_sorted(self):
        """Тест сортування вже відсортованого списку."""
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        
        result = ll.sort()
        
        current = result.head
        expected = [1, 2, 3, 4]
        for val in expected:
            assert current is not None
            assert current.data == val
            current = current.next
        assert current is None
    
    def test_sort_unsorted_list(self):
        """Тест сортування невідсортованого списку."""
        ll = LinkedList()
        ll.append(3)
        ll.append(1)
        ll.append(4)
        ll.append(2)
        ll.append(5)
        
        result = ll.sort()
        
        current = result.head
        expected = [1, 2, 3, 4, 5]
        for val in expected:
            assert current is not None
            assert current.data == val
            current = current.next
        assert current is None
    
    def test_sort_in_place(self):
        """Тест, що sort() змінює поточний список."""
        ll = LinkedList()
        ll.append(3)
        ll.append(1)
        ll.append(2)
        
        original_id = id(ll)
        ll.sort()
        
        assert id(ll) == original_id  # Той самий об'єкт
        assert ll.head.data == 1
        assert ll.head.next.data == 2
        assert ll.head.next.next.data == 3


@pytest.mark.unit
class TestSortedMethod:
    """Тести для методу класу sorted()."""
    
    def test_sorted_empty_list(self):
        """Тест sorted() для порожнього списку."""
        ll = LinkedList()
        result = ll.sorted()
        
        assert result is not ll  # Новий об'єкт
        assert result.head is None
        assert ll.head is None  # Оригінал не змінений
    
    def test_sorted_unsorted_list(self):
        """Тест sorted() для невідсортованого списку."""
        ll = LinkedList()
        ll.append(3)
        ll.append(1)
        ll.append(2)
        
        result = ll.sorted()
        
        # Перевіряємо новий відсортований список
        current = result.head
        expected = [1, 2, 3]
        for val in expected:
            assert current is not None
            assert current.data == val
            current = current.next
        
        # Перевіряємо, що оригінал не змінений
        current = ll.head
        original_values = [3, 1, 2]
        for val in original_values:
            assert current is not None
            assert current.data == val
            current = current.next


@pytest.mark.unit
class TestSortEdgeCases:
    """Тести для крайових випадків сортування."""
    
    def test_sort_reverse_sorted(self):
        """Тест сортування списку, відсортованого в зворотному порядку."""
        ll = LinkedList()
        ll.append(4)
        ll.append(3)
        ll.append(2)
        ll.append(1)
        
        ll.sort()
        
        current = ll.head
        expected = [1, 2, 3, 4]
        for val in expected:
            assert current is not None
            assert current.data == val
            current = current.next
        assert current is None
    
    def test_sort_with_duplicates(self):
        """Тест сортування списку з дублікатами."""
        ll = LinkedList()
        ll.append(3)
        ll.append(1)
        ll.append(3)
        ll.append(2)
        ll.append(1)
        
        ll.sort()
        
        current = ll.head
        expected = [1, 1, 2, 3, 3]
        for val in expected:
            assert current is not None
            assert current.data == val
            current = current.next
        assert current is None
    
    def test_sort_negative_numbers(self):
        """Тест сортування списку з від'ємними числами."""
        ll = LinkedList()
        ll.append(-3)
        ll.append(1)
        ll.append(-1)
        ll.append(2)
        ll.append(-2)
        
        ll.sort()
        
        current = ll.head
        expected = [-3, -2, -1, 1, 2]
        for val in expected:
            assert current is not None
            assert current.data == val
            current = current.next
        assert current is None

