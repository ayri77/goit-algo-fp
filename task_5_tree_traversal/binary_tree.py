"""
Структура бінарного дерева для візуалізації обходів.

Базується на коді з завдання 4 для побудови бінарних дерев.
"""

import uuid
import sys
from pathlib import Path
import random
import importlib.util

# Надійний імпорт Node з task_4 (використовуємо явний шлях до файлу)
task_4_path = Path(__file__).parent.parent / "task_4_heap_visualization"
binary_heap_path = task_4_path / "binary_heap.py"

# Використовуємо importlib для явного імпорту з конкретного файлу
spec = importlib.util.spec_from_file_location("task_4_binary_heap", binary_heap_path)
task_4_binary_heap = importlib.util.module_from_spec(spec)
spec.loader.exec_module(task_4_binary_heap)

Node = task_4_binary_heap.Node  # Імпортуємо Node з task_4

def create_sample_tree() -> Node:
    """
    Створює приклад бінарного дерева для тестування.
    
    Returns:
        Корінь дерева (Node)
        
    Структура дерева:
          0
        /   \
       4     1
      / \   /
     5  10 3
    """
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)
    return root

def create_random_tree(size: int = 10) -> Node:
    """
    Створює випадкове бінарне дерево для тестування.
    
    Args:
        size: Кількість вузлів в дереві
        
    Returns:
        Корінь дерева (Node)
    """
    if size == 0:
        return None
    
    # Генеруємо випадкові значення
    values = [random.randint(0, 100) for _ in range(size)]
    values.sort()
    
    # Створюємо корінь
    root = Node(values[0])
    nodes = [root]
    
    # Додаємо решту вузлів випадковим чином
    for i in range(1, size):
        new_node = Node(values[i])
        nodes.append(new_node)
        
        # Випадково вибираємо батьківський вузол
        parent = random.choice(nodes[:i])  # Вибираємо з існуючих вузлів
        
        # Випадково визначаємо, лівий чи правий нащадок
        if parent.left is None and parent.right is None:
            # Якщо обидва порожні, випадково вибираємо
            if random.random() < 0.5:
                parent.left = new_node
            else:
                parent.right = new_node
        elif parent.left is None:
            parent.left = new_node
        elif parent.right is None:
            parent.right = new_node
        else:
            # Якщо обидва зайняті, випадково замінюємо один
            if random.random() < 0.5:
                parent.left = new_node
            else:
                parent.right = new_node
    
    return root