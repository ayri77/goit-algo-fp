"""
Структура графа для алгоритму Дейкстри.

Містить класи для представлення графа та вершин з вагами ребер.
"""

from typing import Dict, List, Tuple, Optional


class Graph:
    """
    Зважений граф для алгоритму Дейкстри.
    
    Може бути представлений як список суміжності або матриця суміжності.
    """
    
    def __init__(self):
        """
        Ініціалізує порожній граф.
        
        Структура: {вершина: [(сусід, вага), ...]}
        """
        self.vertices: Dict[str, List[Tuple[str, float]]] = {}

    def __iter__(self):
        return iter(self.vertices)

    def add_vertex(self, vertex: str) -> None:
        """
        Додає вершину до графа.
        
        Args:
            vertex: Вершина для додавання
        """
        if vertex not in self.vertices:
            self.vertices[vertex] = []
    
    def add_edge(self, from_vertex: str, to_vertex: str, weight: float) -> None:
        """
        Додає ребро між двома вершинами з вагою.
        
        Args:
            from_vertex: Початкова вершина
            to_vertex: Кінцева вершина
            weight: Вага ребра (відстань)
        """
        
        # Переконуємось, що обидві вершини існують
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)        
        
        # Перевіряємо, чи вже існує ребро до цієї вершини
        neighbors = self.vertices[from_vertex]
        for i, (neighbor, _) in enumerate(neighbors):
            if neighbor == to_vertex:
                # Оновлюємо існуюче ребро
                neighbors[i] = (to_vertex, weight)
                return
        
        # Додаємо нове ребро
        neighbors.append((to_vertex, weight))


    
    def get_neighbors(self, vertex: str) -> List[Tuple[str, float]]:
        """
        Повертає список сусідів вершини з вагами ребер.
        
        Args:
            vertex: Вершина
            
        Returns:
            Список кортежів (сусід, вага)
        """
        return self.vertices.get(vertex, [])

