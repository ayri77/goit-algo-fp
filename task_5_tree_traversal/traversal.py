"""
Алгоритми обходу бінарного дерева: DFS та BFS.

Використовується стек для DFS та черга для BFS (без рекурсії).
"""

from typing import List
try:
    from .binary_tree import Node
except ImportError:
    from binary_tree import Node

from collections import deque


def generate_color(step: int, total_steps: int) -> str:
    """
    Генерує колір у форматі HEX на основі порядку обходу.
    
    Args:
        step: Поточний крок обходу (від 0)
        total_steps: Загальна кількість кроків
        
    Returns:
        Колір у форматі HEX (наприклад, "#1296F0")
        
    Примітка:
        Кольори повинні змінюватися від темних до світлих відтінків.
        Використовуйте 16-систему RGB.
    """
    if total_steps <= 1:
        # Якщо тільки один крок, повертаємо темний колір
        return "#000080"
    
    # Темно-синій: #000080 (R=0, G=0, B=128)
    dark_r, dark_g, dark_b = 0, 0, 128
    
    # Світло-блакитний: #87CEEB (R=135, G=206, B=235)
    light_r, light_g, light_b = 135, 206, 235
    
    # Обчислюємо коефіцієнт інтерполяції (від 0 до 1)
    ratio = step / (total_steps - 1) if total_steps > 1 else 0
    
    # Інтерполюємо між темним та світлим кольором
    r = int(dark_r + (light_r - dark_r) * ratio)
    g = int(dark_g + (light_g - dark_g) * ratio)
    b = int(dark_b + (light_b - dark_b) * ratio)
    
    # Конвертуємо в HEX формат
    return f"#{r:02X}{g:02X}{b:02X}"

def dfs_traversal(root: Node) -> List[Node]:
    """
    Обхід дерева в глибину (Depth-First Search) з використанням стеку.
    
    Args:
        root: Корінь дерева
        
    Returns:
        Список вузлів у порядку обходу DFS
        
    Примітка:
        Використовуйте стек (не рекурсію).
        Можна використати ітеративний підхід з явним стеком.
    """
    if root is None:
        return []
    
    visited = []
    stack = [root]    

    while stack:
        current_node = stack.pop()
        visited.append(current_node)
        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)
    return visited


def bfs_traversal(root: Node) -> List[Node]:
    """
    Обхід дерева в ширину (Breadth-First Search) з використанням черги.
    
    Args:
        root: Корінь дерева
        
    Returns:
        Список вузлів у порядку обходу BFS
        
    Примітка:
        Використовуйте чергу (queue).
    """
    if root is None:
        return []
    
    visited = []
    queue = deque([root])  # Використовуємо чергу з collections
    
    while queue:
        current_node = queue.popleft()
        visited.append(current_node)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    return visited


def apply_colors_to_traversal(nodes: List[Node]):
    """
    Застосовує кольори до вузлів на основі порядку обходу.
    
    Args:
        nodes: Список вузлів у порядку обходу
        
    Примітка:
        Кожен вузол отримує колір на основі його позиції в списку.
        Кольори змінюються від темних до світлих відтінків.
    """
    total = len(nodes)
    for i, node in enumerate(nodes):
        node.color = generate_color(i, total)

