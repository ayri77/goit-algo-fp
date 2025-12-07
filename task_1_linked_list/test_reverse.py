"""
Юніт-тести для реверсування однозв'язного списку.

Перевіряє методи класу reverse() та reversed().
"""

import pytest
import sys
from pathlib import Path

# Додаємо директорію завдання до шляху
sys.path.insert(0, str(Path(__file__).parent))

from linked_list import LinkedList


@pytest.mark.unit
class TestReverseMethod:
    """Тести для методу класу reverse()."""
    
    def test_reverse_empty_list(self):
        """Тест реверсування порожнього списку."""
        ll = LinkedList()
        result = ll.reverse()
        assert result is ll  # Повертає self
        assert result.head is None
    
    def test_reverse_single_element(self):
        """Тест реверсування списку з одним елементом."""
        ll = LinkedList()
        ll.append(1)
        result = ll.reverse()
        
        assert result is ll
        assert result.head is not None
        assert result.head.data == 1
        assert result.head.next is None
    
    def test_reverse_two_elements(self):
        """Тест реверсування списку з двома елементами."""
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        result = ll.reverse()
        
        assert result.head.data == 2
        assert result.head.next.data == 1
        assert result.head.next.next is None
    
    def test_reverse_multiple_elements(self):
        """Тест реверсування списку з кількома елементами."""
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        ll.append(5)
        
        result = ll.reverse()
        
        # Перевіряємо порядок елементів
        current = result.head
        expected_values = [5, 4, 3, 2, 1]
        for expected in expected_values:
            assert current is not None
            assert current.data == expected
            current = current.next
        assert current is None
    
    def test_reverse_in_place(self):
        """Тест, що reverse() змінює поточний список."""
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        
        original_id = id(ll)
        ll.reverse()
        
        assert id(ll) == original_id  # Той самий об'єкт
        assert ll.head.data == 3
        assert ll.head.next.data == 2
        assert ll.head.next.next.data == 1


@pytest.mark.unit
class TestReversedMethod:
    """Тести для методу класу reversed()."""
    
    def test_reversed_empty_list(self):
        """Тест reversed() для порожнього списку."""
        ll = LinkedList()
        result = ll.reversed()
        
        assert result is not ll  # Новий об'єкт
        assert result.head is None
        assert ll.head is None  # Оригінал не змінений
    
    def test_reversed_single_element(self):
        """Тест reversed() для списку з одним елементом."""
        ll = LinkedList()
        ll.append(1)
        result = ll.reversed()
        
        assert result is not ll
        assert result.head.data == 1
        assert ll.head.data == 1  # Оригінал не змінений
    
    def test_reversed_multiple_elements(self):
        """Тест reversed() для списку з кількома елементами."""
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        
        result = ll.reversed()
        
        # Перевіряємо новий список
        current = result.head
        expected_values = [3, 2, 1]
        for expected in expected_values:
            assert current is not None
            assert current.data == expected
            current = current.next
        
        # Перевіряємо, що оригінал не змінений
        current = ll.head
        original_values = [1, 2, 3]
        for expected in original_values:
            assert current is not None
            assert current.data == expected
            current = current.next



