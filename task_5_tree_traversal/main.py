"""
Головний файл для демонстрації обходів бінарного дерева.

Візуалізує обходи DFS та BFS з кольоровим кодуванням.
"""

import sys
from pathlib import Path

# Додаємо шлях до task_5 ПЕРШИМ, щоб локальні модулі знаходилися перед task_4
task_5_path = Path(__file__).parent
if str(task_5_path) not in sys.path:
    sys.path.insert(0, str(task_5_path))

# Імпортуємо модулі (try/except для сумісності з різними способами запуску)
from visualization import draw_tree
from binary_tree import create_random_tree
from traversal import dfs_traversal, bfs_traversal, apply_colors_to_traversal


def main():
    """Демонстрація обходів дерева."""
    
    # Приклад:
    root = create_random_tree(32)
    
    # DFS обхід
    dfs_nodes = dfs_traversal(root)
    apply_colors_to_traversal(dfs_nodes)
    draw_tree(root, "DFS Traversal")
    
    # BFS обхід
    bfs_nodes = bfs_traversal(root)
    apply_colors_to_traversal(bfs_nodes)
    draw_tree(root, "BFS Traversal")    


if __name__ == "__main__":
    main()

