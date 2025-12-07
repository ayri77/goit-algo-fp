"""
Юніт-тести для базового класу LinkedList.

Перевіряє основні операції: append, prepend, display.
"""

import pytest
import sys
from pathlib import Path

# Додаємо корінь проекту до шляху для абсолютних імпортів
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Додаємо директорію завдання до шляху для відносних імпортів
sys.path.insert(0, str(Path(__file__).parent))

try:
    from task_1_linked_list.linked_list import LinkedList, Node
except ImportError:
    from linked_list import LinkedList, Node

@pytest.mark.unit
class TestLinkedList:
    """Тести для класу LinkedList."""
    
    def test_create_empty_list(self):
        """Тест створення порожнього списку."""
        ll = LinkedList()
        assert ll.head is None
    
    def test_append_single_element(self):
        """Тест додавання одного елемента в кінець."""
        ll = LinkedList()
        ll.append(1)
        assert ll.head is not None
        assert ll.head.data == 1
        assert ll.head.next is None
    
    def test_append_multiple_elements(self):
        """Тест додавання кількох елементів в кінець."""
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        
        assert ll.head.data == 1
        assert ll.head.next.data == 2
        assert ll.head.next.next.data == 3
        assert ll.head.next.next.next is None
    
    def test_prepend_single_element(self):
        """Тест додавання одного елемента на початок."""
        ll = LinkedList()
        ll.prepend(1)
        assert ll.head is not None
        assert ll.head.data == 1
        assert ll.head.next is None
    
    def test_prepend_multiple_elements(self):
        """Тест додавання кількох елементів на початок."""
        ll = LinkedList()
        ll.prepend(3)
        ll.prepend(2)
        ll.prepend(1)
        
        assert ll.head.data == 1
        assert ll.head.next.data == 2
        assert ll.head.next.next.data == 3
        assert ll.head.next.next.next is None
    
    def test_prepend_after_append(self):
        """Тест додавання на початок після додавання в кінець."""
        ll = LinkedList()
        ll.append(2)
        ll.append(3)
        ll.prepend(1)
        
        assert ll.head.data == 1
        assert ll.head.next.data == 2
        assert ll.head.next.next.data == 3
    
    def test_str_empty_list(self):
        """Тест рядкового представлення порожнього списку."""
        ll = LinkedList()
        result = str(ll)
        assert result == ""
    
    def test_str_single_element(self):
        """Тест рядкового представлення списку з одним елементом."""
        ll = LinkedList()
        ll.append(1)
        result = str(ll)
        assert result == "1"
    
    def test_str_multiple_elements(self):
        """Тест рядкового представлення списку з кількома елементами."""
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        result = str(ll)
        assert result == "1 -> 2 -> 3"
    
    def test_iter_empty_list(self):
        """Тест ітерації по порожньому списку."""
        ll = LinkedList()
        elements = list(ll)
        assert elements == []
    
    def test_iter_non_empty_list(self):
        """Тест ітерації по непорожньому списку."""
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        elements = [node.data for node in ll]
        assert elements == [1, 2, 3]
    
    def test_len_empty_list(self):
        """Тест довжини порожнього списку."""
        ll = LinkedList()
        assert len(ll) == 0
    
    def test_len_single_element(self):
        """Тест довжини списку з одним елементом."""
        ll = LinkedList()
        ll.append(1)
        assert len(ll) == 1
    
    def test_len_multiple_elements(self):
        """Тест довжини списку з кількома елементами."""
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        assert len(ll) == 3


@pytest.mark.unit
class TestNode:
    """Тести для класу Node."""
    
    def test_create_node(self):
        """Тест створення вузла."""
        node = Node(42)
        assert node.data == 42
        assert node.next is None
    
    def test_link_nodes(self):
        """Тест зв'язування вузлів."""
        node1 = Node(1)
        node2 = Node(2)
        node1.next = node2
        
        assert node1.next == node2
        assert node1.next.data == 2

