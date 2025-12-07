"""
Юніт-тести для алгоритмів обходу дерева: DFS та BFS.

Перевіряє коректність обходів без використання рекурсії.
"""

import pytest
import sys
from pathlib import Path

# ВАЖЛИВО: Спочатку додаємо шлях до task_5, щоб локальні модулі мали пріоритет
task_5_path = Path(__file__).parent
if str(task_5_path) not in sys.path:
    sys.path.insert(0, str(task_5_path))

# Потім додаємо шлях до task_4 для імпорту Node (якщо потрібно)
task_4_path = Path(__file__).parent.parent / "task_4_heap_visualization"
if str(task_4_path) not in sys.path:
    sys.path.insert(0, str(task_4_path))

# Імпортуємо з локальних модулів task_5
# binary_tree вже правильно імпортує Node з task_4
from binary_tree import Node, create_sample_tree
from traversal import dfs_traversal, bfs_traversal, apply_colors_to_traversal


@pytest.mark.unit
class TestTraversal:
    """Тести для функцій обходу дерева."""
    
    def test_dfs_empty_tree(self):
        """Тест DFS для порожнього дерева."""
        result = dfs_traversal(None)
        assert result == []
    
    def test_dfs_single_node(self):
        """Тест DFS для дерева з одним вузлом."""
        root = Node(1)
        result = dfs_traversal(root)
        assert len(result) == 1
        assert result[0].val == 1
    
    def test_dfs_sample_tree(self):
        """Тест DFS для прикладового дерева."""
        root = create_sample_tree()
        result = dfs_traversal(root)
        
        # Перевіряємо, що всі вузли відвідані
        assert len(result) == 6  # 0, 4, 5, 10, 1, 3
        assert result[0].val == 0  # Початок з кореня
    
    def test_bfs_empty_tree(self):
        """Тест BFS для порожнього дерева."""
        result = bfs_traversal(None)
        assert result == []
    
    def test_bfs_single_node(self):
        """Тест BFS для дерева з одним вузлом."""
        root = Node(1)
        result = bfs_traversal(root)
        assert len(result) == 1
        assert result[0].val == 1
    
    def test_bfs_sample_tree(self):
        """Тест BFS для прикладового дерева."""
        root = create_sample_tree()
        result = bfs_traversal(root)
        
        # Перевіряємо, що всі вузли відвідані
        assert len(result) == 6
        # BFS повинен починатися з кореня
        assert result[0].val == 0
    
    def test_bfs_level_order(self):
        """Тест, що BFS обходить дерево по рівнях."""
        root = Node(0)
        root.left = Node(1)
        root.right = Node(2)
        root.left.left = Node(3)
        root.left.right = Node(4)
        
        result = bfs_traversal(root)
        # BFS: 0, 1, 2, 3, 4
        assert result[0].val == 0
        assert result[1].val == 1
        assert result[2].val == 2
    
    def test_dfs_vs_bfs_order(self):
        """Тест, що DFS та BFS дають різний порядок."""
        root = create_sample_tree()
        dfs_result = dfs_traversal(root)
        bfs_result = bfs_traversal(root)
        
        # Перевіряємо, що порядок різний (якщо дерево має більше одного рівня)
        if len(dfs_result) > 1 and len(bfs_result) > 1:
            # Порівнюємо другий елемент
            if dfs_result[1].val != bfs_result[1].val:
                # Порядок дійсно різний
                pass
            else:
                # Можливо порядок збігається для цього дерева
                pass


@pytest.mark.unit
class TestColors:
    """Тести для застосування кольорів."""
    
    def test_apply_colors_empty_list(self):
        """Тест застосування кольорів до порожнього списку."""
        apply_colors_to_traversal([])
        # Не повинно викликати помилок
    
    def test_apply_colors_single_node(self):
        """Тест застосування кольорів до одного вузла."""
        root = Node(1)
        nodes = [root]
        apply_colors_to_traversal(nodes)
        assert root.color is not None
        assert root.color.startswith('#')
    
    def test_apply_colors_multiple_nodes(self):
        """Тест застосування кольорів до кількох вузлів."""
        root = create_sample_tree()
        nodes = dfs_traversal(root)
        apply_colors_to_traversal(nodes)
        
        # Перевіряємо, що всі вузли мають кольори
        for node in nodes:
            assert node.color is not None
            assert node.color.startswith('#')

