"""
Структура бінарної купи для візуалізації.

Містить клас Node та клас BinaryHeap для роботи з купою.
"""

import uuid
from typing import Optional, List
import math


LEVEL_COLORS = {
    0: "skyblue",
    1: "lightgreen",
    2: "lightyellow",
    3: "lightpink",
    4: "lightblue",
    5: "lightgray",
    6: "lightred",
}

def get_index_color(index: int) -> str:
    """
    Отримує колір для вузла за індексом на основі його рівня.
    
    Args:
        index: Індекс вузла в купі
        
    Returns:
        Колір для вузла (за замовчуванням "lightred" для невідомих рівнів)
    """
    level = int(math.log2(index + 1))
    return LEVEL_COLORS.get(level, "lightred")

class Node:
    """
    Вузол бінарної купи.
    
    Attributes:
        val: Значення вузла
        left: Посилання на лівий дочірній вузол
        right: Посилання на правий дочірній вузол
        color: Колір вузла для візуалізації
        id: Унікальний ідентифікатор вузла
    """
    
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

    def __str__(self):
        return f"Node(val={self.val}, color={self.color}, id={self.id})"


class BinaryHeap:
    """
    Бінарна купа (піраміда).
    
    Мінімальна купа: батьківський вузол завжди менший за дочірні.
    """
    
    def __init__(self):
        """Ініціалізує порожню купу."""
        self.heap: List[int] = []
        self.root: Optional[Node] = None
    
    def parent(self, index: int) -> int:
        """Повертає індекс батьківського вузла."""
        return (index - 1) // 2
    
    def left_child_index(self, index: int) -> int:
        """Повертає індекс лівого дочірнього вузла."""
        return 2 * index + 1
    
    def right_child_index(self, index: int) -> int:
        """Повертає індекс правого дочірнього вузла."""
        return 2 * index + 2
    
    def _heapify_up(self, index: int):
        """
        Просіювання вгору для підтримки властивості купи.
        
        Args:
            index: Індекс вузла для просіювання
        """
        while index != 0 and self.heap[self.parent(index)] > self.heap[index]:
            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)

    def _heapify_down(self, index: int):
        """
        Просіювання вниз для підтримки властивості купи.
        
        Args:
            index: Індекс вузла для просіювання
        """
        size = len(self.heap)
        smallest = index
        while True:
            left = self.left_child_index(index)
            right = self.right_child_index(index)

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break

    def insert(self, value: int):
        """
        Додає значення до купи.
        
        Args:
            value: Значення для додавання
        """
        self.heap.append(value)
        self._heapify_up(len(self.heap)-1)   

    def build_tree_from_heap(self) -> Optional[Node]:
        """
        Побудовує дерево з масиву купи для візуалізації.
        
        Returns:
            Корінь дерева (Node) або None, якщо купа порожня
        """
        if not self.heap:
            return None    
        
        # Створити вузли для всіх елементів
        nodes = [Node(val, color=get_index_color(i)) for i, val in enumerate(self.heap)]
        
        for i in range(len(nodes)):
            left_idx = self.left_child_index(i)
            right_idx = self.right_child_index(i)

            # Встановлюємо лівого дитину, якщо він існує
            if left_idx < len(nodes):
                nodes[i].left = nodes[left_idx]
            
            # Встановлюємо правого дитину, якщо він існує
            if right_idx < len(nodes):
                nodes[i].right = nodes[right_idx]                
                
        self.root = nodes[0]

        return self.root

    def extract_min(self) -> Optional[int]:
        """
        Вилучає мінімальний елемент з купи.
        
        Returns:
            Значення мінімального елемента або None, якщо купа порожня
        """
        if not self.heap:
            return None
        
        min_val = self.heap[0]
        
        # Якщо тільки один елемент, просто видаляємо його
        if len(self.heap) == 1:
            self.heap.pop()
            return min_val
        
        # Іначе замінюємо корінь останнім елементом та просіюємо вниз
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return min_val

    def is_empty(self) -> bool:
        """
        Перевіряє, чи є купа порожньою.
        
        Returns:
            True, якщо купа порожня, False в іншому випадку
        """
        return len(self.heap) == 0

    def peek(self) -> Optional[int]:
        """
        Повертає мінімальний елемент без видалення.
        
        Returns:
            Значення мінімального елемента або None, якщо купа порожня
        """
        if not self.heap:
            return None
        return self.heap[0]
