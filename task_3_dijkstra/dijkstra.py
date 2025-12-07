"""
Реалізація алгоритму Дейкстри для знаходження найкоротших шляхів.

Використовує бінарну купу для оптимізації вибору вершин.
"""

from typing import Dict, Optional
try:
    from .graph import Graph
    from .binary_heap import MinHeap
except ImportError:
    from graph import Graph
    from binary_heap import MinHeap

from math import inf

def dijkstra(graph: Graph, start_vertex: str) -> Dict[str, float]:
    """
    Знаходить найкоротші шляхи від початкової вершини до всіх інших.
    
    Args:
        graph: Зважений граф
        start_vertex: Початкова вершина
        
    Returns:
        Словник {вершина: найкоротша відстань} від start_vertex до кожної вершини
        
    Примітка:
        Алгоритм використовує бінарну купу для оптимізації вибору вершини
        з мінімальною відстанню. Складність: O((V + E) log V), де V - вершини, E - ребра.
    """
    distances: Dict[str, float] = {}
    visited: set = set()
    heap = MinHeap()
    
    # Ініціалізуємо відстані та додаємо початкову вершину в купу
    for node in graph:
        distances[node] = inf if node != start_vertex else 0
    
    heap.insert(0, start_vertex)

    while not heap.is_empty():
        current_distance, current_vertex = heap.extract_min()
        
        # Пропускаємо вершини, які вже оброблені
        if current_vertex in visited:
            continue
        
        visited.add(current_vertex)
        
        # Оновлюємо відстані до сусідів
        for neighbor, weight in graph.get_neighbors(current_vertex):
            if neighbor in visited:
                continue
                
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                # Використовуємо decrease_key, якщо вершина вже в купі, інакше insert
                try:
                    heap.decrease_key(neighbor, new_distance)
                except ValueError:
                    # Вершина не в купі, додаємо її
                    heap.insert(new_distance, neighbor)
    
    return distances


def get_shortest_path(graph: Graph, start_vertex: str, end_vertex: str) -> Optional[float]:
    """
    Знаходить найкоротшу відстань між двома вершинами.
    
    Args:
        graph: Зважений граф
        start_vertex: Початкова вершина
        end_vertex: Кінцева вершина
        
    Returns:
        Найкоротша відстань або None, якщо шлях не існує
    """
    distances = dijkstra(graph, start_vertex)
    distance = distances.get(end_vertex)
    # Повертаємо None для недосяжних вершин (відстань = inf)
    if distance is None or distance == inf:
        return None
    return distance

