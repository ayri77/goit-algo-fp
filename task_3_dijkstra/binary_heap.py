"""
Бінарна купа (піраміда) для оптимізації алгоритму Дейкстри.

Використовується як пріоритетна черга для вибору вершини з мінімальною відстанню.
"""

from typing import List, Tuple, Optional


class MinHeap:
    """
    Мінімальна бінарна купа для зберігання пар (відстань, вершина).
    
    Використовується в алгоритмі Дейкстри для ефективного вибору
    вершини з мінімальною відстанню.
    """
    
    def __init__(self):
        """Ініціалізує порожню купу."""
        self.heap: List[Tuple[float, str]] = []
    
    def parent(self, index: int) -> int:
        """Повертає індекс батьківського вузла."""
        return (index - 1) // 2
    
    def left_child(self, index: int) -> int:
        """Повертає індекс лівого дочірнього вузла."""
        return 2 * index + 1
    
    def right_child(self, index: int) -> int:
        """Повертає індекс правого дочірнього вузла."""
        return 2 * index + 2
    
    def swap(self, i: int, j: int):
        """Змінює місцями елементи з індексами i та j."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

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
            left = self.left_child(index)
            right = self.right_child(index)

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break
    
    def insert(self, distance: float, vertex: str):
        """
        Додає елемент до купи з підтримкою властивості купи.
        
        Args:
            distance: Відстань (пріоритет)
            vertex: Вершина
        """
        self.heap.append((distance, vertex))
        self._heapify_up(len(self.heap)-1)    

    def extract_min(self) -> Optional[Tuple[float, str]]:
        """
        Видаляє та повертає елемент з мінімальною відстанню.
        
        Returns:
            Кортеж (відстань, вершина) або None, якщо купа порожня
        """
        if self.is_empty():
            return None            
        minimum = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return minimum

    def is_empty(self) -> bool:
        """Перевіряє, чи купа порожня."""
        return len(self.heap) == 0

    def _find_vertex_index(self, vertex: str) -> Optional[int]:
        """
        Знаходить індекс вершини в купі.
        
        Args:
            vertex: Вершина для пошуку
            
        Returns:
            Індекс вершини в купі або None, якщо вершина не знайдена
        """
        for i, (_, v) in enumerate(self.heap):
            if v == vertex:
                return i
        return None
    
    def decrease_key(self, vertex: str, new_distance: float):
        """
        Зменшує відстань для вершини (якщо вона вже в купі).
        
        Args:
            vertex: Вершина
            new_distance: Нова відстань
        Raises:
            ValueError: Якщо вершина не знайдена в купі
        """
        index = self._find_vertex_index(vertex)
        if index is not None:
            self.heap[index] = (new_distance, vertex)
            self._heapify_up(index)
        else:
            raise ValueError(f"Вершина {vertex} не знайдена в купі")

