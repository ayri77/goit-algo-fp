"""
Юніт-тести для алгоритму Дейкстри.

Перевіряє коректність знаходження найкоротших шляхів.
"""

import pytest
import sys
from pathlib import Path

# Додаємо директорію завдання до шляху
sys.path.insert(0, str(Path(__file__).parent))

from graph import Graph
from dijkstra import dijkstra, get_shortest_path


@pytest.mark.unit
class TestDijkstra:
    """Тести для функції dijkstra."""
    
    def test_single_vertex(self):
        """Тест для графа з однією вершиною."""
        graph = Graph()
        graph.add_vertex('A')
        distances = dijkstra(graph, 'A')
        assert distances['A'] == 0.0
    
    def test_two_vertices(self):
        """Тест для графа з двома вершинами."""
        graph = Graph()
        graph.add_vertex('A')
        graph.add_vertex('B')
        graph.add_edge('A', 'B', 5.0)
        
        distances = dijkstra(graph, 'A')
        assert distances['A'] == 0.0
        assert distances['B'] == 5.0
    
    def test_linear_graph(self):
        """Тест для лінійного графа A -> B -> C."""
        graph = Graph()
        graph.add_vertex('A')
        graph.add_vertex('B')
        graph.add_vertex('C')
        graph.add_edge('A', 'B', 2.0)
        graph.add_edge('B', 'C', 3.0)
        
        distances = dijkstra(graph, 'A')
        assert distances['A'] == 0.0
        assert distances['B'] == 2.0
        assert distances['C'] == 5.0
    
    def test_graph_with_multiple_paths(self):
        """Тест для графа з кількома шляхами до однієї вершини."""
        graph = Graph()
        graph.add_vertex('A')
        graph.add_vertex('B')
        graph.add_vertex('C')
        graph.add_edge('A', 'B', 5.0)
        graph.add_edge('A', 'C', 2.0)
        graph.add_edge('C', 'B', 1.0)
        
        distances = dijkstra(graph, 'A')
        assert distances['A'] == 0.0
        assert distances['C'] == 2.0
        assert distances['B'] == 3.0  # Через C, а не напряму
    
    def test_disconnected_vertex(self):
        """Тест для графа з від'єднаною вершиною."""
        graph = Graph()
        graph.add_vertex('A')
        graph.add_vertex('B')
        graph.add_vertex('C')
        graph.add_edge('A', 'B', 1.0)
        # C не з'єднана з іншими
        
        distances = dijkstra(graph, 'A')
        assert distances['A'] == 0.0
        assert distances['B'] == 1.0
        # C повинна мати нескінченну відстань або не бути в результатах
        # Залежить від реалізації


@pytest.mark.unit
class TestGetShortestPath:
    """Тести для функції get_shortest_path."""
    
    def test_path_exists(self):
        """Тест знаходження існуючого шляху."""
        graph = Graph()
        graph.add_vertex('A')
        graph.add_vertex('B')
        graph.add_vertex('C')
        graph.add_edge('A', 'B', 2.0)
        graph.add_edge('B', 'C', 3.0)
        
        distance = get_shortest_path(graph, 'A', 'C')
        assert distance == 5.0
    
    def test_path_not_exists(self):
        """Тест для неіснуючого шляху."""
        graph = Graph()
        graph.add_vertex('A')
        graph.add_vertex('B')
        # Немає ребра між A та B
        
        distance = get_shortest_path(graph, 'A', 'B')
        assert distance is None
    
    def test_same_start_and_end(self):
        """Тест для шляху від вершини до самої себе."""
        graph = Graph()
        graph.add_vertex('A')
        
        distance = get_shortest_path(graph, 'A', 'A')
        assert distance == 0.0

