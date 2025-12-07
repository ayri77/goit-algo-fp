"""
Юніт-тести для об'єднання відсортованих однозв'язних списків.

Перевіряє статичний метод LinkedList.merge() та метод merge_with().
"""

import pytest
import sys
from pathlib import Path

# Додаємо директорію завдання до шляху
sys.path.insert(0, str(Path(__file__).parent))

from linked_list import LinkedList


@pytest.mark.unit
class TestMergeStaticMethod:
    """Тести для статичного методу LinkedList.merge()."""
    
    def test_merge_empty_lists(self):
        """Тест об'єднання двох порожніх списків."""
        list1 = LinkedList()
        list2 = LinkedList()
        result = LinkedList.merge(list1, list2)
        assert result.head is None
    
    def test_merge_sorted_lists(self):
        """Тест об'єднання двох відсортованих списків."""
        list1 = LinkedList()
        list1.append(1)
        list1.append(3)
        list1.append(5)
        
        list2 = LinkedList()
        list2.append(2)
        list2.append(4)
        list2.append(6)
        
        result = LinkedList.merge(list1, list2)
        
        current = result.head
        expected = [1, 2, 3, 4, 5, 6]
        for val in expected:
            assert current is not None
            assert current.data == val
            current = current.next
        assert current is None
    
    def test_merge_original_lists_unchanged(self):
        """Тест, що оригінальні списки не змінюються."""
        list1 = LinkedList()
        list1.append(1)
        list1.append(3)
        
        list2 = LinkedList()
        list2.append(2)
        list2.append(4)
        
        result = LinkedList.merge(list1, list2)
        
        # Перевіряємо, що оригінали не змінені
        assert list1.head.data == 1
        assert list1.head.next.data == 3
        assert list2.head.data == 2
        assert list2.head.next.data == 4


@pytest.mark.unit
class TestMergeWithMethod:
    """Тести для методу екземпляра merge_with()."""
    
    def test_merge_with(self):
        """Тест методу merge_with()."""
        list1 = LinkedList()
        list1.append(1)
        list1.append(3)
        list1.append(5)
        
        list2 = LinkedList()
        list2.append(2)
        list2.append(4)
        list2.append(6)
        
        result = list1.merge_with(list2)
        
        current = result.head
        expected = [1, 2, 3, 4, 5, 6]
        for val in expected:
            assert current is not None
            assert current.data == val
            current = current.next
        assert current is None


@pytest.mark.unit
class TestMergeEdgeCases:
    """Тести для крайових випадків об'єднання."""
    
    def test_merge_first_empty(self):
        """Тест об'єднання, коли перший список порожній."""
        list1 = LinkedList()
        list2 = LinkedList()
        list2.append(1)
        list2.append(2)
        list2.append(3)
        
        result = LinkedList.merge(list1, list2)
        
        current = result.head
        expected = [1, 2, 3]
        for val in expected:
            assert current is not None
            assert current.data == val
            current = current.next
        assert current is None
    
    def test_merge_second_empty(self):
        """Тест об'єднання, коли другий список порожній."""
        list1 = LinkedList()
        list1.append(1)
        list1.append(2)
        list1.append(3)
        list2 = LinkedList()
        
        result = LinkedList.merge(list1, list2)
        
        current = result.head
        expected = [1, 2, 3]
        for val in expected:
            assert current is not None
            assert current.data == val
            current = current.next
        assert current is None
    
    def test_merge_single_elements(self):
        """Тест об'єднання списків з одним елементом кожен."""
        list1 = LinkedList()
        list1.append(1)
        list2 = LinkedList()
        list2.append(2)
        
        result = LinkedList.merge(list1, list2)
        
        assert result.head.data == 1
        assert result.head.next.data == 2
        assert result.head.next.next is None
    
    def test_merge_overlapping_values(self):
        """Тест об'єднання списків з перетинаючимися значеннями."""
        list1 = LinkedList()
        list1.append(1)
        list1.append(3)
        list1.append(5)
        
        list2 = LinkedList()
        list2.append(2)
        list2.append(3)
        list2.append(4)
        
        result = LinkedList.merge(list1, list2)
        
        current = result.head
        expected = [1, 2, 3, 3, 4, 5]
        for val in expected:
            assert current is not None
            assert current.data == val
            current = current.next
        assert current is None
    
    def test_merge_different_lengths(self):
        """Тест об'єднання списків різної довжини."""
        list1 = LinkedList()
        list1.append(1)
        list1.append(5)
        
        list2 = LinkedList()
        list2.append(2)
        list2.append(3)
        list2.append(4)
        list2.append(6)
        list2.append(7)
        
        result = LinkedList.merge(list1, list2)
        
        current = result.head
        expected = [1, 2, 3, 4, 5, 6, 7]
        for val in expected:
            assert current is not None
            assert current.data == val
            current = current.next
        assert current is None
    
    def test_merge_all_from_first(self):
        """Тест, коли всі елементи першого списку менші."""
        list1 = LinkedList()
        list1.append(1)
        list1.append(2)
        list1.append(3)
        
        list2 = LinkedList()
        list2.append(4)
        list2.append(5)
        list2.append(6)
        
        result = LinkedList.merge(list1, list2)
        
        current = result.head
        expected = [1, 2, 3, 4, 5, 6]
        for val in expected:
            assert current is not None
            assert current.data == val
            current = current.next
        assert current is None
    
    def test_merge_all_from_second(self):
        """Тест, коли всі елементи другого списку менші."""
        list1 = LinkedList()
        list1.append(4)
        list1.append(5)
        list1.append(6)
        
        list2 = LinkedList()
        list2.append(1)
        list2.append(2)
        list2.append(3)
        
        result = LinkedList.merge(list1, list2)
        
        current = result.head
        expected = [1, 2, 3, 4, 5, 6]
        for val in expected:
            assert current is not None
            assert current.data == val
            current = current.next
        assert current is None

